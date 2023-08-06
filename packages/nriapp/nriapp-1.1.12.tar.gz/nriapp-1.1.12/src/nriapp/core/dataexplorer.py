from azure.kusto.data import KustoConnectionStringBuilder, DataFormat
from azure.kusto.ingest import QueuedIngestClient, IngestionProperties, FileDescriptor, BlobDescriptor
from datetime import timedelta

from azure.kusto.data import KustoClient, KustoConnectionStringBuilder, ClientRequestProperties
from azure.kusto.data.exceptions import KustoServiceError
from azure.kusto.data.helpers import dataframe_from_result_table
from azure.identity import DeviceCodeCredential
import json
import pandas as pd
import os
import concurrent.futures
from tqdm import tqdm
import pickle, cloudpickle
from datetime import date

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

session_file = os.path.abspath(os.path.dirname(__file__)) + "\..\session\kusto.pkl"
tenant_id = "bcf2d2a2-2dee-419b-971f-21e5170fbf84"
KUSTO_URI = "https://kvcw1z66xgnuy00q1uhhzs.australiaeast.kusto.windows.net"
KUSTO_INGEST_URI = "https://ingest-kvcw1z66xgnuy00q1uhhzs.australiaeast.kusto.windows.net"

class DataIngestion():
    def __init__(self, kusto_uri=KUSTO_URI, kusto_ingest_uri=KUSTO_INGEST_URI, tenant_id=tenant_id):
        device_credential  = DeviceCodeCredential(authority="https://login.microsoftonline.com/", tenant_id=tenant_id)
        if os.path.exists(os.path.abspath(session_file)):
            with open(session_file, 'rb') as f:
                self.token = pickle.load(f)  
        else: 
            self.token = device_credential.get_token("https://help.kusto.windows.net/.default").token
            with open(session_file, 'wb') as f:
                pickle.dump(self.token, f)  
        kcsb_query = KustoConnectionStringBuilder.with_aad_device_authentication(KUSTO_URI, self.token)
        kcsb_ingest = KustoConnectionStringBuilder.with_aad_device_authentication(KUSTO_INGEST_URI, self.token)
        kcsb_query.authority_id = tenant_id
        kcsb_ingest.authority_id = tenant_id
        self.client_query = KustoClient(kcsb_query)
        self.client_ingest = QueuedIngestClient(kcsb_ingest)

    def ingest_raw(self, data, ingestion_props):
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for data_element in tqdm(data):
                df = pd.DataFrame({"raw": [json.dumps(data_element)]})
                future = executor.submit(self.client_ingest.ingest_from_dataframe(df, ingestion_props))
                futures.append(future)

    def ingest_events(self, data, database="Incidents", table="Raw"):
  
        check_changes = '''
        Raw
        | extend a = parse_json(Events)
        | distinct items= tostring(a)
        | extend a = parse_json(items)
        | project IncidentId=toint(a.IncidentId), Status=toint(a.Status)
        | sort by IncidentId desc 
        '''

        response = self.client_query.execute(database, check_changes)
        
        results = response.primary_results[0]

        set1 = set(json.dumps({"id":x["IncidentId"], "value": x["Status"]}, sort_keys=True) for x in results) #Serialize
        set2 = set(json.dumps({"id":x["IncidentId"], "value": x["Status"]}, sort_keys=True) for x in data)    #Serialize

        diff = [json.loads(x)["id"] for x in set2.difference(set1)]    #Deserialize

        diff = ', '.join(str(i) for i in diff)

        if diff:
            remove_list = '''
            .delete table Raw records <|
            Raw
            | extend item = parse_json(Events)
            | where toint(item.IncidentId) in (''' + diff + ''')
            '''
            response = self.client_query.execute(database, remove_list)

        incident_list = ''' 
        Raw
        | extend a = parse_json(Events)
        | distinct items= tostring(a)
        | extend a = parse_json(items)
        | project toint(a.IncidentId)
        ''' 
        response = self.client_query.execute(database, incident_list)        
        event_ids = [i[0] for i in response.primary_results[0].raw_rows]

        to_ingest = [i["IncidentId"] for i in data]

    #    unique = sorted(list(set(ids).difference(to_ingest)))
        similar = sorted(list(set(event_ids).intersection(to_ingest)))

        for i in data[:]:
            if i["IncidentId"] in similar:
                data.remove(i)

        path = os.path.join(desktop, "incidents.tmp")
        with open(path, "w") as file:
            for item in data:
                file.write(json.dumps(item) + "\n")
        if data:
            ingestion_props = IngestionProperties(database=database,table=table,data_format=DataFormat.MULTIJSON, ingestion_mapping_reference="RawEventMapping")
            self.client_ingest.ingest_from_file(path, ingestion_properties=ingestion_props)
        os.remove(path)
        return data


    def ingest_mfastats(self, data, database="Incidents", table="Multifactor"):
        item_list = '''
        Multifactor
        | extend items = parse_json(Items)
        | project items.ID
        '''
        response = self.client_query.execute(database, item_list)
        user_ids = [i[0] for i in response.primary_results[0].raw_rows]
        ingestion_props = IngestionProperties(database=database,table=table,data_format=DataFormat.JSON)
        self.ingest_raw(data, ingestion_props)

    def ingest_audit_logs(self, data, database="Incidents", table="AuditHistory"):
        to_ingest = [i["id"] for i in data]
        pending = ', '.join(str(i) for i in to_ingest)
        if not pending:
            return data
        remove_list = '''
        .delete table AuditHistory records <|
        AuditHistory
        | extend item = parse_json(Items)
        | where toint(item.id) in (''' + pending + ''')
        '''
        response = self.client_query.execute(database, remove_list)

        path = os.path.join(desktop, "audit.tmp")
        with open(path, "w") as file:
            for item in data:
                file.write(json.dumps(item) + "\n")
        if data:
            ingestion_props = IngestionProperties(database=database,table=table,data_format=DataFormat.MULTIJSON, ingestion_mapping_reference="AuditHistoryMapping")
            self.client_ingest.ingest_from_file(path, ingestion_properties=ingestion_props)
        os.remove(path)
        return data    

    def check_ingest_users_tag(self, database="Incidents", table="AzureAD"):
        tag = date.today().strftime("%Y-%m-%d")

        current_tags = '''
        AzureAD
        | extend tags = tostring(extent_tags())
        | distinct tags
        | extend item = parse_json(tags)
        | mv-expand tag = item
        | project trim_start("ingest-by:", tostring(tag))
        '''
        response = self.client_query.execute(database, current_tags)        
        tags = [i[0] for i in response.primary_results[0].raw_rows]
        for i in tags:
            if tag == i:
                return True
        return False

    def ingest_users(self, data, database="Incidents", table="AzureAD"):
        tag = date.today().strftime("%Y-%m-%d")

        current_tags = '''
        AzureAD
        | extend tags = tostring(extent_tags())
        | distinct tags
        | extend item = parse_json(tags)
        | mv-expand tag = item
        | project trim_start("ingest-by:", tostring(tag))
        '''
        response = self.client_query.execute(database, current_tags)        
        tags = [i[0] for i in response.primary_results[0].raw_rows]
        for i in tags:
            if tag == i:
                return
        path = os.path.join(desktop, "users.tmp")
        with open(path, "w") as file:
            for item in data:
                file.write(json.dumps(item) + "\n")
        if data:
            ingestion_props = IngestionProperties(database=database,table=table,data_format=DataFormat.MULTIJSON, ingestion_mapping_reference="FlatEventMapping", ingest_if_not_exists=[tag],ingest_by_tags=[tag], drop_by_tags=[tag])
            self.client_ingest.ingest_from_file(path, ingestion_properties=ingestion_props)
        os.remove(path)

    def check_ingest_devices_tags(self, database="Incidents", table="IntuneDevices"):
        tag = date.today().strftime("%Y-%m-%d")

        current_tags = '''
        IntuneDevices
        | extend tags = tostring(extent_tags())
        | distinct tags
        | extend item = parse_json(tags)
        | mv-expand tag = item
        | project trim_start("ingest-by:", tostring(tag))
        '''
        response = self.client_query.execute(database, current_tags)        
        tags = [i[0] for i in response.primary_results[0].raw_rows]
        for i in tags:
            if tag == i:
                return True
        return False

    def ingest_devices(self, data, database="Incidents", table="IntuneDevices"):
        tag = date.today().strftime("%Y-%m-%d")

        current_tags = '''
        IntuneDevices
        | extend tags = tostring(extent_tags())
        | distinct tags
        | extend item = parse_json(tags)
        | mv-expand tag = item
        | project trim_start("ingest-by:", tostring(tag))
        '''
        response = self.client_query.execute(database, current_tags)        
        tags = [i[0] for i in response.primary_results[0].raw_rows]
        for i in tags:
            if tag == i:
                return
        path = os.path.join(desktop, "devices.tmp")
        with open(path, "w") as file:
            for item in data:
                file.write(json.dumps(item) + "\n")
        if data:
            ingestion_props = IngestionProperties(database=database,table=table,data_format=DataFormat.MULTIJSON, ingestion_mapping_reference="IntuneDevicesMapping", ingest_if_not_exists=[tag],ingest_by_tags=[tag], drop_by_tags=[tag])
            self.client_ingest.ingest_from_file(path, ingestion_properties=ingestion_props)
        os.remove(path)

    def check_ingest_managed_devices_tag(self, database="Incidents", table="ManagedDevices"):
        tag = date.today().strftime("%Y-%m-%d")

        current_tags = '''
        ManagedDevices
        | extend tags = tostring(extent_tags())
        | distinct tags
        | extend item = parse_json(tags)
        | mv-expand tag = item
        | project trim_start("ingest-by:", tostring(tag))
        '''
        response = self.client_query.execute(database, current_tags)        
        tags = [i[0] for i in response.primary_results[0].raw_rows]
        for i in tags:
            if tag == i:
                return True
        return False

    def ingest_managed_devices(self, data, database="Incidents", table="ManagedDevices"):
        tag = date.today().strftime("%Y-%m-%d")

        current_tags = '''
        ManagedDevices
        | extend tags = tostring(extent_tags())
        | distinct tags
        | extend item = parse_json(tags)
        | mv-expand tag = item
        | project trim_start("ingest-by:", tostring(tag))
        '''
        response = self.client_query.execute(database, current_tags)        
        tags = [i[0] for i in response.primary_results[0].raw_rows]
        for i in tags:
            if tag == i:
                return

        path = os.path.join(desktop, "managedDevices.tmp")
        with open(path, "w") as file:
            for item in data:
                file.write(json.dumps(item) + "\n")
        if data:
            ingestion_props = IngestionProperties(database=database,table=table,data_format=DataFormat.MULTIJSON, ingestion_mapping_reference="ManagedDevicesMapping", ingest_if_not_exists=[tag],ingest_by_tags=[tag], drop_by_tags=[tag]) 
            self.client_ingest.ingest_from_file(path, ingestion_properties=ingestion_props)
        os.remove(path)


    def ingest_defender_agents(self, path, database="Incidents", table="DefenderAgents"):
        tag = date.today().strftime("%Y-%m-%d")

        ingestion_props =  IngestionProperties(database=database,table=table,data_format=DataFormat.CSV, ingestion_mapping_reference="DefenderAgents_mapping", additional_properties={'ignoreFirstRecord': 'true'},  ingest_if_not_exists=[tag],ingest_by_tags=[tag], drop_by_tags=[tag]) 
        result = self.client_ingest.ingest_from_file(path, ingestion_properties=ingestion_props)
        os.remove(path)
        return result   



    kusto_query = '''
    let minimum = toscalar (
    Raw
    | extend a = parse_json(Events)
    | top 1 by toint(a.IncidentId) asc
    );
    let maximum = toscalar (
    Raw
    | extend a = parse_json(Events)
    | top 1 by toint(a.IncidentId) desc 
    );
    print highest=maximum.IncidentId,lowest=minimum.IncidentId;
    '''



#    for i in data[:]:
#        if i["IncidentId"] in similar:
#            data.remove(i)

#    response = client_query.execute(DATABASE, kusto_query)
#    row = response.primary_results[0].rows[0]
#    highest = row[0]
#    lowest = row[1]

    #json_str = json.dumps({"Events": data})
    #jsonFile = open("data.json", "w")
    #jsonFile.write(json_str)
    #jsonFile.close()

#    with open("data.json", "w") as file:
#        for i in data:
#            file.write(json.dumps(i) + '\n')

#    df = pd.DataFrame({"events": [json.dumps({"Events": data})]})
#    df = pd.DataFrame({"events": [json.dumps(my_dict)]})
#    df = pd.DataFrame({"events": [json.dumps(data[3])]})
#    ingestion_props = IngestionProperties(database="Incidents",table="Raw",data_format=DataFormat.JSON, ingestion_mapping_reference="Ewan")
#    ingestion_props = IngestionProperties(database="Incidents",table="Raw",data_format=DataFormat.JSON, ingestion_mapping_reference="RawMap")
#    file_descriptor = FileDescriptor ("data.json", os.stat("data.json").st_size)#
#    client_ingest.ingest_from_file(file_descriptor, ingestion_properties=ingestion_props)


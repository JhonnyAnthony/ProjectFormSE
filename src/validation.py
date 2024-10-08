import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

load_dotenv()
class ValidationAPI:
   # function to declare api, url variables and doing the authorization
    def __init__(self, api_id, url):
        self.api_id = api_id
        self.url = url
        self.headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": "urn:workflow#getWorkflow",
            "Authorization": api_id,
            "Content-Length": "287",
            "Host": "sesuiteqas.fgm.ind.br",
            "Connection": "Keep-Alive",
        }

    def get_workflow(self, process_id, user_id):
        soap_envelope = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
            <soapenv:Header/>
            <soapenv:Body>
                <urn:newWorkflow>
                    <urn:ProcessID>{process_id}</urn:ProcessID>
                    <urn:WorkflowTitle>Teste!!</urn:WorkflowTitle>
                    <urn:UserID>{user_id}</urn:UserID>
                </urn:newWorkflow>
            </soapenv:Body>
        </soapenv:Envelope>
        """
      # 
        response = requests.post(self.url, data=soap_envelope, headers=self.headers)
      # IF response is 200 -> Working!
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            return root
        else:
            raise Exception(f"Error: {response.status_code}")

    def print_workflow(self, workflow_id):
        root = self.get_workflow(workflow_id)
      #Print all variables usable
        for child in root.iter("*"):
         print(child.tag, child.text)
        if root is not None:
            # Search for the record_id and print it 
            record_id = root.find('.//urn:RecordID', namespaces={'urn': 'urn:workflow'})
            if record_id is not None:
                print(f"RecordID: {record_id.text}")
            else:
                print("RecordID not found")
        else:
            print("No response received")
      

        
# Usage
api_id = os.getenv("MY_API_ID")
user_id = os.getenv("MY_USER_ID")
url = os.getenv("MY_URL")
workflow_id = "120034"
process_id = os.getenv("MY_PROCESS_ID")
api = ValidationAPI(api_id, url)
api.print_workflow(workflow_id)

import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..','src', 'venv', '.env')
load_dotenv(dotenv_path)

class ValidationAPI:
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
        self.process_id = os.getenv("MY_PROCESS_ID")

    def get_workflow(self, process_id,nome):
        soap_envelope = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
            <soapenv:Header/>
            <soapenv:Body>
                <urn:newWorkflow>
                    <urn:ProcessID>{process_id}</urn:ProcessID>
                    <urn:WorkflowTitle>Desligamento{nome}</urn:WorkflowTitle>
                    <urn:UserID>jhonny.souza</urn:UserID>
                </urn:newWorkflow>
            </soapenv:Body>
        </soapenv:Envelope>
        """
        response = requests.post(self.url, data=soap_envelope, headers=self.headers)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            print(response.status_code)
            return root
        elif response.status_code == 401:
            print(response.status_code)
            raise Exception(f"Error: {response.status_code}")

    def RecordID(self):
        root = self.get_workflow(self.process_id)
        if root is not None:
            record_id = root.find('.//urn:RecordID', namespaces={'urn': 'urn:workflow'})
            if record_id is not None:
                print(f"RecordID: {record_id.text}")
                return record_id.text
            else:
                print("RecordID not found")
        else:
            print("No response received")

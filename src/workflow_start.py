import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'venv', '.env')
load_dotenv(dotenv_path)
process_id = os.getenv("PROCESS_ID")
api_id = os.getenv("MY_API_ID")
url = os.getenv("MY_URL")
user = os.getenv("MY_USER")
class ValidationAPI:
    def __init__(self):
        self.api_id = api_id
        self.url = url
        self.user = user
        self.process_id = process_id
        self.headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": "urn:workflow#getWorkflow",
            "Authorization": self.api_id,
            "Host": "sesuiteqas.fgm.ind.br",
            "Connection": "Keep-Alive",
        }

    def get_workflow(self):
        soap_envelope = f'''<?xml version="1.0" encoding="UTF-8"?>
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
            <soapenv:Header/>
            <soapenv:Body>
                <urn:newWorkflow>
                    <urn:ProcessID>{self.process_id}</urn:ProcessID>
                    <urn:WorkflowTitle>Desligamento</urn:WorkflowTitle>
                    <urn:UserID>{self.user}</urn:UserID>
                </urn:newWorkflow>
            </soapenv:Body>
        </soapenv:Envelope>'''

        self.headers["Content-Length"] = str(len(soap_envelope.encode('utf-8')))

        response = requests.post(self.url, data=soap_envelope.encode('utf-8'), headers=self.headers)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            return root
        else:
            print(f"Error: {response.status_code}")
            return None

    def RecordID(self):
        root = self.get_workflow()
        if root is not None:
            record_id = root.find('.//urn:RecordID', namespaces={'urn': 'urn:workflow'})
            if record_id is not None:
                print(f"RecordID: {record_id.text}")
                return record_id.text
            else:
                print("RecordID not found")
        else:
            print("No response received")

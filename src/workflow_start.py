import requests
import xml.etree.ElementTree as ET
from config import process_id,api_id,url,user,Host
import logging
class ValidationAPI: 
    def __init__(self):
        self.api_id = api_id
        self.url = url
        self.headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "Content-Length": "287",
            "SOAPAction": "urn:workflow#getWorkflow",
            "Authorization": self.api_id,
            "Host": Host,
            "Connection": "Keep-Alive",
        }

    def get_workflow(self, nome):
        soap_envelope = f'''<?xml version="1.0" encoding="UTF-8"?>
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
            <soapenv:Header/>
            <soapenv:Body>
                <urn:newWorkflow>
                    <urn:ProcessID>{process_id}</urn:ProcessID>
                    <urn:WorkflowTitle>Entrevista de Desligamento de {nome}</urn:WorkflowTitle>
                    <urn:UserID>{user}</urn:UserID>
                </urn:newWorkflow>
            </soapenv:Body>
        </soapenv:Envelope>'''
        print(soap_envelope)
        self.headers["Content-Length"] = str(len(soap_envelope.encode('utf-8')))
        response = requests.post(self.url, data=soap_envelope.encode('utf-8'), headers=self.headers)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            record_id = root.find('.//urn:RecordID', namespaces={'urn': 'urn:workflow'})
            if record_id is not None:
                logging.info(f"RecordID: {record_id.text}")
                return record_id.text
            else:
                logging.error("RecordID not found")
                return None
        else:
            logging.error(f"Error {response.status_code}: {response.content} - Workflow")
            return None

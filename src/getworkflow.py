import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'venv', '.env')
load_dotenv(dotenv_path)
process_id = os.getenv("PROCESS_ID")
api_id = os.getenv("MY_API_ID")
url = os.getenv("MY_URL")

class ValidationAPI:
    def __init__(self):
        self.api_id = api_id
        self.url = url
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
                <urn:getWorkflow>
                    <urn:WorkflowID></urn:WorkflowID>
                </urn:getWorkflow>
            </soapenv:Body>
        </soapenv:Envelope>'''
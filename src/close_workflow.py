import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'venv', '.env')
load_dotenv(dotenv_path)


# Get API ID and URL from environment variables
api_id = os.getenv("MY_API_ID")
url = os.getenv("MY_URL")
user = os.getenv("MY_USER")


class CloseWorkflow:
    # Function to declare API, URL variables and perform authorization
    def __init__(self):
        self.api_id = api_id
        self.url = url
        self.user = user
        self.headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "Content-Length": "287",
            "SOAPAction": "urn:workflow#newWorkflow",
            "Authorization": self.api_id,
            "Host": "sesuiteqas.fgm.ind.br",
            "Connection": "Keep-Alive",
        }




    def close_workflow(self, record_id):

        soap_envelope = f"""<?xml version="1.0" encoding="UTF-8"?>
                    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
                        <soapenv:Header/>
                        <soapenv:Body>
                            <urn:executeActivity>
                                <urn:WorkflowID>{record_id}</urn:WorkflowID>
                                <urn:ActivityID>atv01</urn:ActivityID>
                                <urn:ActionSequence>1</urn:ActionSequence>
                                <urn:UserID>{self.user}</urn:UserID>
                            </urn:executeActivity>
                        </soapenv:Body>
                    </soapenv:Envelope>
 
            """
        
        # print(soap_envelope)
        self.headers["Content-Length"] = str(len(soap_envelope.encode('utf-8')))

        response = requests.post(self.url, data=soap_envelope.encode('utf-8'), headers=self.headers)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            print(response.content)
            return response.text
        else:
            print(f"Error: {response.status_code}")
            return None
                
                
  
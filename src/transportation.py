import requests
import xml.etree.ElementTree as ET
from config import api_id,url,Host
import logging

class Transportation:
    def __init__(self):
        self.api_id = api_id
        self.url = url
        self.headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "Content-Length": "287",
            "SOAPAction": "urn:workflow#editEntityRecord",
            "Authorization": self.api_id,
            "Host": Host,
            "Connection": "Keep-Alive",
        }



        #Get the variables declared on main
    def edit_workflow(self, record_id, nome,data_demissao,setor,cargo,iniciativa_desligamento,motivodesliga,
                    beneficios,beneficiostxt,avalia_ambiente_fgm,dms_consideracoes_04,orientacao,gestao,indicaria_fgm,dms_consideracoes_11,
                    mensagemparafgm,comunicacao,avaliacaojornada,dms_consideracoes_01,mudancastrab,comunicatxt,treinamentos,
                    oportunidades,consilideranca,feedback,):

        soap_envelope = f"""
                    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
                        <soapenv:Header/>
                        <soapenv:Body>
                            <urn:editEntityRecord>
                                <urn:WorkflowID>{record_id}</urn:WorkflowID>
                                <urn:EntityID>dlc02</urn:EntityID>
                                <urn:EntityAttributeList>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>nomcol</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{nome}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                </urn:EntityAttributeList>
                            </urn:editEntityRecord>
                        </soapenv:Body>
                        </soapenv:Envelope>
            """
        soap_envelope = soap_envelope.replace("&", "&amp;")
        # print(soap_envelope)
        self.headers["Content-Length"] = str(len(soap_envelope.encode('utf-8')))

        response = requests.post(self.url, data=soap_envelope.encode('utf-8'), headers=self.headers)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            namespace = {'soap': 'http://schemas.xmlsoap.org/soap/envelope/', 'ns': 'urn:workflow'}
            status = root.find('.//ns:Status', namespace).text
            code = root.find('.//ns:Code', namespace).text
            detail = root.find('.//ns:Detail', namespace).text
            logging.info(f"Status: {status}, Code: {code}, Detail: {detail} de {nome} Transportation")
            return response.text
        else:
            logging.error(f"Error {response.status_code}: {response.content} - Transportation")
        return None

                
  
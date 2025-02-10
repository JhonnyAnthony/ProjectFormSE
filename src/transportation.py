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
                    beneficios,beneficiostxt,avalia_ambiente_fgm,dms_consideracoes_04,orientacao,gestao,indicaria_fgm,recomendatxt,
                    mensagemparafgm,comunicacao,avaliacaojornada,dms_consideracoes_01,mudancastrab,comunicatxt,treinamentos,
                    oportunidades,consilideranca,feedback,beneficiosrelev):

        soap_envelope = f''' 
                
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
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>datademiss</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{data_demissao}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>setor</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{setor}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>cargo</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{cargo}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>motivodesliga</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{motivodesliga}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>demaisconsi1</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{dms_consideracoes_01}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>beneficiostxt</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{beneficiostxt}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>demaisconsi4</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{dms_consideracoes_04}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>mudancastrab</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{mudancastrab}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>comunicatxt</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{comunicatxt}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>treinamentos</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{treinamentos}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>oportunidades</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{oportunidades}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>consiliderenca</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{consilideranca}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>feedback</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{feedback}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>recomendatxt</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{recomendatxt}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>mensagemparafgm</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{mensagemparafgm}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>gestaopessoas</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{gestao}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                        <urn:EntityAttributeID>beneficiosrelev</urn:EntityAttributeID>
                                        <urn:EntityAttributeValue>{beneficiosrelev}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                </urn:EntityAttributeList>
                                <urn:RelationshipList>
                                    <urn:Relationship>
                                    <urn:RelationshipID>iniciativadesli</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>empregado</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{iniciativa_desligamento}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                </urn:Relationship>
                                <urn:Relationship>
                                    <urn:RelationshipID>avaliacaojornad</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas1</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avaliacaojornada}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                </urn:Relationship>
                                <urn:Relationship>
                                    <urn:RelationshipID>benefi</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{beneficios}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                </urn:Relationship>
                                <urn:Relationship>
                                    <urn:RelationshipID>avaliaambiente</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_ambiente_fgm}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                </urn:Relationship>
                                
                                <urn:Relationship>
                                    <urn:RelationshipID>comunicacao</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{comunicacao}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                </urn:Relationship>
                                <urn:Relationship>
                                    <urn:RelationshipID>orientacao</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{orientacao}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                </urn:Relationship>
                                <urn:Relationship>
                                    <urn:RelationshipID>indicafgm</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{indicaria_fgm}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                </urn:Relationship>
                                </urn:RelationshipList>                                
                            </urn:editEntityRecord>
                        </soapenv:Body>
                    </soapenv:Envelope>
            '''
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

                

import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os
from workflow_start import ValidationAPI

api_id = os.getenv("MY_API_ID")
validation_api = ValidationAPI(api_id)
        # Call the method to get RecordID
record_id = validation_api.RecordID()
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'venv', '.env')
load_dotenv(dotenv_path)


# Get API ID and URL from environment variables
url = os.getenv("MY_URL")
EntityID = os.getenv("ENTITYID")
class Transportation:
    # Function to declare API, URL variables and perform authorization
    def __init__(self, api_id):
        self.api_id = api_id
        self.url = url
        self.headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": "urn:workflow#editAttributeValue",
            "Authorization": self.api_id,
            "Host": "sesuiteqas.fgm.ind.br",
            "Connection": "Keep-Alive",
        }




    def edit_workflow(self, record_id, nome, data_admissao, data_demissao, cargo, iniciativa_desligamento, motivo_desligamento, avalia_fgm,
                             dms_consideracoes_01, avalia_estrutura_fgm, dms_consideracoes_02, avalia_ambiente_fgm, dms_consideracoes_03, avalia_setor, dms_consideracoes_04,
                             vale_transporte, vale_refeicao, plano_saude_medico, plano_saude_odontologico, convenio_farmacia, convenio_odonto, presente_aniversario,
                             vacina, seguro_vida, bolsa_estudo, dms_consideracoes_05, avalia_atuacao_cargo, dms_consideracoes_06, avalia_recursos, dms_consideracoes_07,
                             avalia_gestao, dms_consideracoes_08, avalia_comunicacao_interna, avalia_endomarketing, avalia_treinamentos, avalia_recrutamento_interno,
                             avalia_suporte_folhas, avalia_segurança_trabalho, avalia_canal_ouvidoria, avalia_ccq, avalia_Onboarding, dms_consideracoes_09, voltaria_para_fgm,
                             dms_consideracoes_10, indicaria_fgm, dms_consideracoes_11, mensagem_fgm, setor,presente_nascimento,presente_casamento):

    
        soap_envelope = f"""
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
                    <soapenv:Header/>
                    <soapenv:Body>
                        <urn:editEntityRecord>
                            <!--You may enter the following 5 items in any order-->
                            <urn:WorkflowID>?</urn:WorkflowID>
                            <urn:EntityID>?</urn:EntityID>
                            <!--Optional:-->
                            <urn:EntityAttributeList>
                                <!--Zero or more repetitions:-->
                                <urn:EntityAttribute>
                                <!--You may enter the following 2 items in any order-->
                                <urn:EntityAttributeID>?</urn:EntityAttributeID>
                                <urn:EntityAttributeValue>?</urn:EntityAttributeValue>
                                </urn:EntityAttribute>
                            </urn:EntityAttributeList>
                            <!--Optional:-->
                            <urn:RelationshipList>
                                <!--Zero or more repetitions:-->
                                <urn:Relationship>
                                <urn:RelationshipID>?</urn:RelationshipID>
                                <!--1 or more repetitions:-->
                                <urn:RelationshipAttribute>
                                    <!--You may enter the following 2 items in any order-->
                                    <urn:RelationshipAttributeID>?</urn:RelationshipAttributeID>
                                    <urn:RelationshipAttributeValue>?</urn:RelationshipAttributeValue>
                                </urn:RelationshipAttribute>
                                </urn:Relationship>
                            </urn:RelationshipList>
                            <!--Optional:-->
                            <urn:EntityAttributeFileList>
                                <!--Zero or more repetitions:-->
                                <urn:EntityAttributeFile>
                                <!--You may enter the following 3 items in any order-->
                                <urn:EntityAttributeID>?</urn:EntityAttributeID>
                                <urn:FileName>?</urn:FileName>
                                <urn:FileContent>cid:399494657558</urn:FileContent>
                                </urn:EntityAttributeFile>
                            </urn:EntityAttributeFileList>
                        </urn:editEntityRecord>
                    </soapenv:Body>
                </soapenv:Envelope>
            """
        print(soap_envelope)
        # print(soap_envelope)
        response = requests.post(self.url, data=soap_envelope, headers=self.headers)
        if response.status_code == 200:
                root = ET.fromstring(response.content)
                print(response.content)
                return root
        elif response.status_code == 401:
                print(response.status_code)
                raise Exception(f"Error: {response.status_code}")
        
   
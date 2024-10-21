import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'venv', '.env')
load_dotenv(dotenv_path)


# Get API ID and URL from environment variables
api_id = os.getenv("MY_API_ID")
url = os.getenv("MY_URL")


class Transportation:
    # Function to declare API, URL variables and perform authorization
    def __init__(self):
        self.api_id = api_id
        self.url = url
        self.headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "Content-Length": "287",
            "SOAPAction": "urn:workflow#editEntityRecord",
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
                             dms_consideracoes_10, dms_consideracoes_11, mensagem_fgm, setor,presente_nascimento,presente_casamento,indicaria_fgm):

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
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>dataadmiss</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{data_admissao}</urn:EntityAttributeValue>
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
                                    <urn:EntityAttributeValue>{motivo_desligamento}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>demaisconsi1</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{dms_consideracoes_01}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>demaisconsi2</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{dms_consideracoes_02}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>demaisconsi4</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{dms_consideracoes_03}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>demaisconsid4</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{dms_consideracoes_04}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>demaisconsi5</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{dms_consideracoes_05}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>demaisconsi6</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{dms_consideracoes_06}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>demaisconsi7</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{dms_consideracoes_07}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>demaisconsi8</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{dms_consideracoes_08}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>demaisconsi9</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{dms_consideracoes_09}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>demaisconsi10</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{dms_consideracoes_10}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>demaisconsi11</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{dms_consideracoes_11}</urn:EntityAttributeValue>
                                    </urn:EntityAttribute>
                                    <urn:EntityAttribute>
                                    <urn:EntityAttributeID>mensagemparafgm</urn:EntityAttributeID>
                                    <urn:EntityAttributeValue>{mensagem_fgm}</urn:EntityAttributeValue>
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
                                        <urn:RelationshipAttributeValue>{avalia_fgm}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>avaliacaoestrut</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_estrutura_fgm}</urn:RelationshipAttributeValue>
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
                                    <urn:RelationshipID>avaambiente2</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_setor}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>valtransp</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{vale_transporte}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>valerefrest</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{vale_refeicao}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>plansaude</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{plano_saude_medico}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>odontopl</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{plano_saude_odontologico}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>farma</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{convenio_farmacia}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>odonto</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{convenio_odonto}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>aniversario</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{presente_aniversario}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>casamento</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{presente_casamento}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>nascimento</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{presente_nascimento}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>vacinagripe</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{vacina}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>segurovida</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{seguro_vida}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>estudo</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{bolsa_estudo}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>classificacao</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_atuacao_cargo}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>avaliarecursos</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_recursos}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>avaliagestao</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_gestao}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>comunicacao</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_comunicacao_interna}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>endomkt</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_endomarketing}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>treinamedesenvo</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_treinamentos}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>recruta</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_recrutamento_interno}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>suportefolha</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_suporte_folhas}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>segurancatrab</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_segurança_trabalho}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>ouvidoria</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_canal_ouvidoria}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>ccq</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_ccq}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>onboarding</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{avalia_Onboarding}</urn:RelationshipAttributeValue>
                                    </urn:RelationshipAttribute>
                                    </urn:Relationship>
                                    <urn:Relationship>
                                    <urn:RelationshipID>voltariatrab</urn:RelationshipID>
                                    <urn:RelationshipAttribute>
                                        <urn:RelationshipAttributeID>escolhas</urn:RelationshipAttributeID>
                                        <urn:RelationshipAttributeValue>{voltaria_para_fgm}</urn:RelationshipAttributeValue>
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
            """
        
        # print(soap_envelope)
        response = requests.post(self.url, data=soap_envelope, headers=self.headers)
        # print(response.content)
        
        if response.status_code == 200:
                
                root = ET.fromstring(response.content)
                print(response.content)
                return response.text
        elif response.status_code == 401:
                print(response.status_code)
                raise Exception(f"Error: {response.status_code}")
        else:
            return response
        
   
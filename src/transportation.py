import requests
import os
import openpyxl
import pandas as pd
import xml.etree.ElementTree as ET


class transportation:
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
def update_excel_path(new_file_name):
        base_path = r'C:\Users\jhonny.souza\Downloads'
        return os.path.join(base_path, new_file_name)
excel_path = update_excel_path('Entrevista Maio.xlsx')
# Carregar a planilha do Excel
df = pd.read_excel(excel_path, skiprows=2)
workbook = openpyxl.load_workbook(excel_path)
    # Obter a primeira planilha
sheet = workbook.active
print(df)

#define o caminho do arquivo
# Função para ler e imprimir os dados das células específicas
def responses_variable():
    for row_idx in range(2, sheet.max_row, +1):
                    id                                      = sheet[f'A{row_idx}'].value
                    hora_inicio                             = sheet[f'B{row_idx}'].value
                    hora_conclusao                          = sheet[f'C{row_idx}'].value
                    email                                   = sheet[f'D{row_idx}'].value
                    nome                                    = sheet[f'F{row_idx}'].value
                    data_admissao                           = sheet[f'G{row_idx}'].value
                    data_demissao                           = sheet[f'H{row_idx}'].value
                    setor                                   = sheet[f'I{row_idx}'].value
                    cargo                                   = sheet[f'J{row_idx}'].value
                    iniciativa_desligamento                 = sheet[f'K{row_idx}'].value
                    motivo_desligamento                     = sheet[f'L{row_idx}'].value 
                    avalia_fgm                              = sheet[f'M{row_idx}'].value
                    dms_consideracoes_01                    = sheet[f'N{row_idx}'].value 
                    avalia_estrutura_fgm                    = sheet[f'O{row_idx}'].value
                    dms_consideracoes_02                    = sheet[f'P{row_idx}'].value
                    avalia_ambiente_fgm                     = sheet[f'Q{row_idx}'].value
                    dms_consideracoes_03                    = sheet[f'R{row_idx}'].value
                    avalia_setor                            = sheet[f'S{row_idx}'].value
                    dms_consideracoes_04                    = sheet[f'T{row_idx}'].value
                    vale_transporte                         = sheet[f'U{row_idx}'].value
                    vale_refeicao                           = sheet[f'V{row_idx}'].value
                    plano_saude_medico                      = sheet[f'W{row_idx}'].value
                    plano_saude_odontologico                = sheet[f'X{row_idx}'].value
                    convenio_farmacia                       = sheet[f'Y{row_idx}'].value
                    convenio_odonto                         = sheet[f'Z{row_idx}'].value
                    presente_aniversario                    = sheet[f'AA{row_idx}'].value
                    presente_casamento                      = sheet[f'AB{row_idx}'].value
                    presente_nascimento                     = sheet[f'AC{row_idx}'].value
                    vacina                                  = sheet[f'AD{row_idx}'].value
                    seguro_vida                             = sheet[f'AE{row_idx}'].value
                    bolsa_estudo                            = sheet[f'AF{row_idx}'].value
                    dms_consideracoes_05                    = sheet[f'AG{row_idx}'].value
                    avalia_atuacao_cargo                    = sheet[f'AH{row_idx}'].value
                    dms_consideracoes_06                    = sheet[f'AI{row_idx}'].value
                    avalia_recursos                         = sheet[f'AJ{row_idx}'].value
                    dms_consideracoes_07                    = sheet[f'AK{row_idx}'].value
                    avalia_gestao                           = sheet[f'AL{row_idx}'].value
                    dms_consideracoes_08                    = sheet[f'AM{row_idx}'].value
                    avalia_comunicacao_interna              = sheet[f'AN{row_idx}'].value
                    avalia_endomarketing                    = sheet[f'AO{row_idx}'].value
                    avalia_treinamentos                     = sheet[f'AP{row_idx}'].value
                    avalia_recrutamento_interno             = sheet[f'AQ{row_idx}'].value
                    avalia_suporte_folhas                   = sheet[f'AR{row_idx}'].value
                    avalia_segurança_trabalho               = sheet[f'AS{row_idx}'].value
                    avalia_canal_ouvidoria                  = sheet[f'AT{row_idx}'].value
                    avalia_ccq                              = sheet[f'AU{row_idx}'].value
                    avalia_Onboarding                       = sheet[f'AV{row_idx}'].value
                    dms_consideracoes_09                    = sheet[f'AW{row_idx}'].value
                    voltaria_para_fgm                       = sheet[f'AX{row_idx}'].value
                    dms_consideracoes_10                    = sheet[f'AY{row_idx}'].value
                    indicaria_fgm                           = sheet[f'AZ{row_idx}'].value
                    dms_consideracoes_11                    = sheet[f'BA{row_idx}'].value
                    mensagem_fgm                            = sheet[f'BB{row_idx}'].value

                    
    def edit_workflow(self, id,nome,data_admissao,data_demissao,cargo,iniciativa_desligamento,motivo_desligamento,avalia_fgm,
        dms_consideracoes_01, avalia_estrutura_fgm,dms_consideracoes_02,avalia_ambiente_fgm,dms_consideracoes_03,avalia_setor,dms_consideracoes_04,
        vale_transporte,vale_refeicao,plano_saude_medico,plano_saude_odontologico,convenio_farmacia,convenio_odonto,presente_aniversario,
        vacina,seguro_vida,bolsa_estudo,dms_consideracoes_05,avalia_atuacao_cargo,dms_consideracoes_06,avalia_recursos,dms_consideracoes_07,
        avalia_gestao,dms_consideracoes_08,avalia_comunicacao_interna,avalia_endomarketing,avalia_treinamentos,avalia_recrutamento_interno,
        avalia_suporte_folhas,avalia_segurança_trabalho,avalia_canal_ouvidoria,avalia_ccq,avalia_Onboarding,dms_consideracoes_09,voltaria_para_fgm ,
        dms_consideracoes_10,indicaria_fgm,dms_consideracoes_11,mensagem_fgm):
        soap_envelope = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
                <soapenv:Header/>
                <soapenv:Body>
                    <urn:editEntityRecord>
                        <urn:WorkflowID>dcl001</urn:WorkflowID>
                        <urn:EntityID>{id}</urn:EntityID>
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
                            <urn:EntityAttributeID>demaisconsi3</urn:EntityAttributeID>
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
                                <urn:RelationshipAttributeValue>{iniciativa_desligamento }</urn:RelationshipAttributeValue>
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
                                <urn:RelationshipAttributeValue>{plano_saude_odontologico }</urn:RelationshipAttributeValue>
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
                </soapenv:Envelope>"""
        edit_workflow()
        response = requests.post(self.url, data=soap_envelope, headers=self.headers)
      # IF response is 200 -> Working!
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            print(root)
            return root
        else:
            raise Exception(f"Error: {response.status_code}")

api = transportation(api_id=os.getenv("MY_API_ID"), url=os.getenv("MY_URL"))
responses_variable()
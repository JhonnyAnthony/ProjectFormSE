import os
from dotenv import load_dotenv
from reader_xlsx import ExcelDataReader
from transportation import Transportation
from workflow_start import ValidationAPI
from datetime import datetime
from dbconect import DatabaseDataReader
from integration_excel import IntegrationOneDrive
# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'venv', '.env')
load_dotenv(dotenv_path)

# # Retrieve the variables
server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
client_id = os.getenv("MY_CLIENT_ID")
client_secret = os.getenv("MY_CLIENT_SECRET")
tenant_id = os.getenv("MY_TENANT_ID")
link = os.getenv("LINK_AUTHORITY")
authority = f"{link}{tenant_id}"

# Downloader excel file
integration = IntegrationOneDrive(client_id, client_secret, authority)
integration.download()

# Create an instance of ExcelDataReader
reader = ExcelDataReader('Entrevista de Desligamento.xlsx', 'Sheet1')
reader.load_data()



# Connection string
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
# Create an instance of DatabaseDataReader
db_reader = DatabaseDataReader(connection_string)
db_reader.load_data()

# Get all row data
se_data = db_reader.get_se_row_data()

# Close the connection
db_reader.close_connection()
# # for row_data_excel in se_data:

# # Get all row data where the name is not null
excel_data = reader.get_excel_row_data()


def send_se(row_data_excel):
    # Create an instance of Transportation
    transport = Transportation()

    # Instantiate the ValidationAPI class
    validation_api = ValidationAPI()

    # While here send to SE
    try:
        # print(vars(row_data_excel))
        # Fetch RecordID for each row if needed
        record_id = validation_api.RecordID()
        # record_id = '077618'
        

        if isinstance(row_data_excel.data_admissao, str):
            data_admissao = datetime.strptime(row_data_excel.data_admissao, "%Y-%m-%d")
        else:
            data_admissao = row_data_excel.data_admissao
            
        if isinstance(row_data_excel.data_demissao, str):
            data_demissao = datetime.strptime(row_data_excel.data_demissao, "%Y-%m-%d")
        else:
            data_demissao = row_data_excel.data_demissao
        # Format dates to yyyy-MM-dd
        formatted_data_admissao = row_data_excel.data_admissao.strftime("%Y-%m-%d")
        formatted_data_demissao = row_data_excel.data_demissao.strftime("%Y-%m-%d")

        # Debugging: Print the record_id and row_data_excel to check for duplicates
        # print(f"Processing RecordID: {record_id}, Row Data: {row_data_excel}")

        # Call edit_workflow method with the fetched record_id and row data
        transport.edit_workflow(
            record_id                   =record_id,
            nome                        =row_data_excel.nome,
            data_admissao               =formatted_data_admissao,
            data_demissao               =formatted_data_demissao,
            setor                       =row_data_excel.setor,
            cargo                       =row_data_excel.cargo,
            iniciativa_desligamento     =row_data_excel.iniciativa_desligamento,
            motivo_desligamento         =row_data_excel.motivo_desligamento,
            avalia_fgm                  =row_data_excel.avalia_fgm,
            dms_consideracoes_01        =row_data_excel.dms_consideracoes_01,
            avalia_estrutura_fgm        =row_data_excel.avalia_estrutura_fgm,
            dms_consideracoes_02        =row_data_excel.dms_consideracoes_02,
            avalia_ambiente_fgm         =row_data_excel.avalia_ambiente_fgm,
            dms_consideracoes_03        =row_data_excel.dms_consideracoes_03,
            avalia_setor                =row_data_excel.avalia_setor,
            dms_consideracoes_04        =row_data_excel.dms_consideracoes_04,
            vale_transporte             =row_data_excel.vale_transporte,
            vale_refeicao               =row_data_excel.vale_refeicao,
            plano_saude_medico          =row_data_excel.plano_saude_medico,
            plano_saude_odontologico    =row_data_excel.plano_saude_odontologico,
            convenio_farmacia           =row_data_excel.convenio_farmacia,
            convenio_odonto             =row_data_excel.convenio_odonto,
            presente_aniversario        =row_data_excel.presente_aniversario,
            vacina                      =row_data_excel.vacina,
            seguro_vida                 =row_data_excel.seguro_vida,
            bolsa_estudo                =row_data_excel.bolsa_estudo,
            dms_consideracoes_05        =row_data_excel.dms_consideracoes_05,
            avalia_atuacao_cargo        =row_data_excel.avalia_atuacao_cargo,
            dms_consideracoes_06        =row_data_excel.dms_consideracoes_06,
            avalia_recursos             =row_data_excel.avalia_recursos,
            dms_consideracoes_07        =row_data_excel.dms_consideracoes_07,
            avalia_gestao               =row_data_excel.avalia_gestao,
            dms_consideracoes_08        =row_data_excel.dms_consideracoes_08,
            avalia_comunicacao_interna  =row_data_excel.avalia_comunicacao_interna,
            avalia_endomarketing        =row_data_excel.avalia_endomarketing,
            avalia_treinamentos         =row_data_excel.avalia_treinamentos,
            avalia_recrutamento_interno =row_data_excel.avalia_recrutamento_interno,
            avalia_suporte_folhas       =row_data_excel.avalia_suporte_folhas,
            avalia_segurança_trabalho   =row_data_excel.avalia_segurança_trabalho,
            avalia_canal_ouvidoria      =row_data_excel.avalia_canal_ouvidoria,
            avalia_ccq                  =row_data_excel.avalia_ccq,
            avalia_Onboarding           =row_data_excel.avalia_Onboarding,
            dms_consideracoes_09        =row_data_excel.dms_consideracoes_09,
            voltaria_para_fgm           =row_data_excel.voltaria_para_fgm,
            dms_consideracoes_10        =row_data_excel.dms_consideracoes_10,
            indicaria_fgm               =row_data_excel.indicaria_fgm,
            dms_consideracoes_11        =row_data_excel.dms_consideracoes_11,
            mensagem_fgm                =row_data_excel.mensagem_fgm,
            presente_nascimento         =row_data_excel.presente_nascimento,
            presente_casamento          =row_data_excel.presente_casamento
            )
            
    except Exception as e:
        print(f"An error occurred: {e}")
            
for row_data_excel in excel_data:
    for row_data_se in se_data:
        print(f"primeiro valor: {row_data_excel.nome} segundo valor: {row_data_se.nome_colaborador}")
        if row_data_se.nome_colaborador == row_data_excel.nome:
            print()
        else:  
            # envio_se(row_data_excel)
            print("chegou aqui")
            print(row_data_excel.nome)


import os
import logging
from config import server,database,username,sheet,file_name,password,client_id,client_secret,authority
from reader_xlsx import ExcelDataReader
from transportation import Transportation
from workflow_start import ValidationAPI
from datetime import datetime
from dbconect import DatabaseDataReader
from integration_excel import IntegrationOneDrive
from close_workflow import CloseWorkflow

def logs():
    # Define the directory path where logs will be stored
    log_directory = r"C:\Github\ProjectFormSE\Logs"
        # Create the log directory if it doesn't exist
    if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Get the current date and time
    current_datetime = datetime.now()

            # Generate a filename based on the current date within the log folder
    log_filename = os.path.join(log_directory, current_datetime.strftime("%Y-%m-%d") + "_log.log")

            # Configure logging to output to this filename
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=log_filename  # Use the generated filename within the log folder
    )
    
logs()

# Downloader excel file
integration = IntegrationOneDrive(client_id, client_secret, authority)
integration.download()

# Create an instance of ExcelDataReader
reader = ExcelDataReader(f'{file_name}', f'{sheet}')
reader.excel_data()
excel_data = reader.get_excel_row_data()

# Connection string
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
db_reader = DatabaseDataReader(connection_string)
db_reader.load_database()
se_data = db_reader.get_se_row_data()          

counter = 0
for row_data_excel in excel_data:
    # Instance create only to make a bool to validade duplicates
    nome_duplicado = False
    for row_data_se in se_data:
        # Valid if has a name and a data already in SE
        if row_data_se.nome_colaborador == row_data_excel.nome and row_data_se.data_demissao == row_data_excel.data_demissao:
            nome_duplicado = True
            logging.info(f"{row_data_excel.nome} already on SE")
            break
        # If name is already in SE checking if the data is different, if is gonna reverse the instance to continue scripting
        elif  row_data_se.data_demissao != row_data_excel.data_demissao:
                nome_duplicado = False  
    if nome_duplicado:
        continue

    transport = Transportation() # Create an instance of Transportation
    validation_api = ValidationAPI() # Instantiate the ValidationAPI class
    close = CloseWorkflow() # Calls closeworkflow
    
    try: # Here send to SE
        counter += 1
        print(f"Executing Script - Wait Finish!, {counter}: Script Running")
        logs()
        
        
        record_id = validation_api.get_workflow(row_data_excel.nome)# Fetch RecordID for each row if needed and put nome in workflow
        # record_id = '077939' #Just for tests
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
        # Calls closer_workflow
        closer = close.close_workflow(
            record_id = record_id,
        )
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
print("Script Finished!") #When loop finish stop and print finished


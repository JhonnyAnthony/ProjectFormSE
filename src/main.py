import os
import logging
from config import server,database,username,sheet,file_name,password,client_id,client_secret,authority,driver
from reader_xlsx import ExcelDataReader
from transportation import Transportation
from workflow_start import ValidationAPI
from datetime import datetime
from dbconect import DatabaseDataReader
from integration_excel import IntegrationOneDrive
from close_workflow import CloseWorkflow

def logs():
    # Define the directory path where logs will be stored
    log_directory = r"C:/Github/ProjectFormSE/Logs"
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
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
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
        print(f"Testando {counter}")
        record_id = validation_api.get_workflow(row_data_excel.nome)# Fetch RecordID for each row if needed and put nome in workflow
        # record_id = '077939' #Just for tests
                    
        if isinstance(row_data_excel.data_demissao, str):
            data_demissao = datetime.strptime(row_data_excel.data_demissao, "%Y-%m-%d")
        else:
            data_demissao = row_data_excel.data_demissao
        # Format dates to yyyy-MM-dd
        formatted_data_demissao = row_data_excel.data_demissao.strftime("%Y-%m-%d")

        # Call edit_workflow method with the fetched record_id and row data
        transport.edit_workflow(
            record_id                           =record_id,
            nome                                =row_data_excel.nome,
            data_demissao                       =formatted_data_demissao,
            setor                               =row_data_excel.setor,
            cargo                               =row_data_excel.cargo,
            iniciativa_desligamento             =row_data_excel.iniciativa_desligamento,
            motivodesliga                       =row_data_excel.motivodesliga,
            avaliacaojornada                    =row_data_excel.avaliacaojornada,
            dms_consideracoes_01                =row_data_excel.dms_consideracoes_01,
            beneficios                          =row_data_excel.beneficios,
            beneficiostxt                       =row_data_excel.beneficiostxt,
            avalia_ambiente_fgm                 =row_data_excel.avalia_ambiente_fgm,
            dms_consideracoes_04                =row_data_excel.dms_consideracoes_04,
            mudancastrab                        =row_data_excel.mudancastrab,
            comunicacao                         =row_data_excel.comunicacao,
            comunicatxt                         =row_data_excel.comunicatxt,
            treinamentos                        =row_data_excel.treinamentos,
            oportunidades                       =row_data_excel.oportunidades,
            orientacao                          =row_data_excel.orientacao,
            consilideranca                      =row_data_excel.consilideranca,
            feedback                            =row_data_excel.feedback,
            gestao                              =row_data_excel.gestao,
            indicaria_fgm                       =row_data_excel.indicaria_fgm,
            recomendatxt                        =row_data_excel.recomendatxt,
            mensagemparafgm                     =row_data_excel.mensagemparafgm,
            )
        # Calls closer_workflow
        # closer = close.close_workflow(
        #     record_id = record_id,
        # )
        
    except Exception as e:
        logging.error(f"An error occurred: {e} - MAIN" )
print("Script Finished!") #When loop finish stop and print finished


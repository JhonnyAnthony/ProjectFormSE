import os
from dotenv import load_dotenv
from reader_xlsx import ExcelDataReader
from transportation import Transportation
from workflow_start import ValidationAPI
from datetime import datetime

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'venv', '.env')
load_dotenv(dotenv_path)

# Create an instance of ExcelDataReader
reader = ExcelDataReader('Entrevista de Desligamento.xlsx', 'Sheet1')
reader.load_data()


# # for row_data in row_data_list:

# Get all row data where the name is not null
all_row_data = reader.get_all_row_data()

# Create an instance of Transportation
transport = Transportation()

# Instantiate the ValidationAPI class
validation_api = ValidationAPI()

for row_data in all_row_data:
    try:
        # print(vars(row_data))
        # Fetch RecordID for each row if needed
        record_id = validation_api.RecordID()
        # record_id = '077618'
        

        if isinstance(row_data.data_admissao, str):
            data_admissao = datetime.strptime(row_data.data_admissao, "%Y-%m-%d")
        else:
            data_admissao = row_data.data_admissao
        
        if isinstance(row_data.data_demissao, str):
            data_demissao = datetime.strptime(row_data.data_demissao, "%Y-%m-%d")
        else:
            data_demissao = row_data.data_demissao
        # Format dates to yyyy-MM-dd
        formatted_data_admissao = row_data.data_admissao.strftime("%Y-%m-%d")
        formatted_data_demissao = row_data.data_demissao.strftime("%Y-%m-%d")

        # Debugging: Print the record_id and row_data to check for duplicates
        # print(f"Processing RecordID: {record_id}, Row Data: {row_data}")

        # Call edit_workflow method with the fetched record_id and row data
        transport.edit_workflow(
            record_id                   =record_id,
            nome                        =row_data.nome,
            data_admissao               =formatted_data_admissao,
            data_demissao               =formatted_data_demissao,
            setor                       =row_data.setor,
            cargo                       =row_data.cargo,
            iniciativa_desligamento     =row_data.iniciativa_desligamento,
            motivo_desligamento         =row_data.motivo_desligamento,
            avalia_fgm                  =row_data.avalia_fgm,
            dms_consideracoes_01        =row_data.dms_consideracoes_01,
            avalia_estrutura_fgm        =row_data.avalia_estrutura_fgm,
            dms_consideracoes_02        =row_data.dms_consideracoes_02,
            avalia_ambiente_fgm         =row_data.avalia_ambiente_fgm,
            dms_consideracoes_03        =row_data.dms_consideracoes_03,
            avalia_setor                =row_data.avalia_setor,
            dms_consideracoes_04        =row_data.dms_consideracoes_04,
            vale_transporte             =row_data.vale_transporte,
            vale_refeicao               =row_data.vale_refeicao,
            plano_saude_medico          =row_data.plano_saude_medico,
            plano_saude_odontologico    =row_data.plano_saude_odontologico,
            convenio_farmacia           =row_data.convenio_farmacia,
            convenio_odonto             =row_data.convenio_odonto,
            presente_aniversario        =row_data.presente_aniversario,
            vacina                      =row_data.vacina,
            seguro_vida                 =row_data.seguro_vida,
            bolsa_estudo                =row_data.bolsa_estudo,
            dms_consideracoes_05        =row_data.dms_consideracoes_05,
            avalia_atuacao_cargo        =row_data.avalia_atuacao_cargo,
            dms_consideracoes_06        =row_data.dms_consideracoes_06,
            avalia_recursos             =row_data.avalia_recursos,
            dms_consideracoes_07        =row_data.dms_consideracoes_07,
            avalia_gestao               =row_data.avalia_gestao,
            dms_consideracoes_08        =row_data.dms_consideracoes_08,
            avalia_comunicacao_interna  =row_data.avalia_comunicacao_interna,
            avalia_endomarketing        =row_data.avalia_endomarketing,
            avalia_treinamentos         =row_data.avalia_treinamentos,
            avalia_recrutamento_interno =row_data.avalia_recrutamento_interno,
            avalia_suporte_folhas       =row_data.avalia_suporte_folhas,
            avalia_segurança_trabalho   =row_data.avalia_segurança_trabalho,
            avalia_canal_ouvidoria      =row_data.avalia_canal_ouvidoria,
            avalia_ccq                  =row_data.avalia_ccq,
            avalia_Onboarding           =row_data.avalia_Onboarding,
            dms_consideracoes_09        =row_data.dms_consideracoes_09,
            voltaria_para_fgm           =row_data.voltaria_para_fgm,
            dms_consideracoes_10        =row_data.dms_consideracoes_10,
            indicaria_fgm               =row_data.indicaria_fgm,
            dms_consideracoes_11        =row_data.dms_consideracoes_11,
            mensagem_fgm                =row_data.mensagem_fgm,
            presente_nascimento         =row_data.presente_nascimento,
            presente_casamento          =row_data.presente_casamento
        )
        
    except Exception as e:
        print(f"An error occurred: {e}")
        # Log the error and continue with the next row
        continue

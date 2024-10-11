from reader_xlsx import ExcelDataReader, RowData
from transportation import Transportation
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Get file name and base path from environment variables
file_name = os.getenv("FILE_NAME")
base_path = os.getenv("BASE_PATH")

# Create an instance of ExcelDataReader

reader = ExcelDataReader(file_name, base_path)

# Get all row data where the name is not null
all_row_data = reader.get_all_row_data()

# Get API ID and URL from environment variables
api_id = os.getenv("MY_API_ID")
url = os.getenv("MY_URL")

# Create an instance of the transportation class
transport = Transportation(api_id, url)

# Iterate over all_row_data and call edit_workflow for each row
for row_data in all_row_data:
    transport.edit_workflow(
        id=row_data.id,
        nome=row_data.nome,
        data_admissao=row_data.data_admissao,
        data_demissao=row_data.data_demissao,
        cargo=row_data.cargo,
        iniciativa_desligamento=row_data.iniciativa_desligamento,
        motivo_desligamento=row_data.motivo_desligamento,
        avalia_fgm=row_data.avalia_fgm,
        dms_consideracoes_01=row_data.dms_consideracoes_01,
        avalia_estrutura_fgm=row_data.avalia_estrutura_fgm,
        dms_consideracoes_02=row_data.dms_consideracoes_02,
        avalia_ambiente_fgm=row_data.avalia_ambiente_fgm,
        dms_consideracoes_03=row_data.dms_consideracoes_03,
        avalia_setor=row_data.avalia_setor,
        dms_consideracoes_04=row_data.dms_consideracoes_04,
        vale_transporte=row_data.vale_transporte,
        vale_refeicao=row_data.vale_refeicao,
        plano_saude_medico=row_data.plano_saude_medico,
        plano_saude_odontologico=row_data.plano_saude_odontologico,
        convenio_farmacia=row_data.convenio_farmacia,
        convenio_odonto=row_data.convenio_odonto,
        presente_aniversario=row_data.presente_aniversario,
        vacina=row_data.vacina,
        seguro_vida=row_data.seguro_vida,
        bolsa_estudo=row_data.bolsa_estudo,
        dms_consideracoes_05=row_data.dms_consideracoes_05,
        avalia_atuacao_cargo=row_data.avalia_atuacao_cargo,
        dms_consideracoes_06=row_data.dms_consideracoes_06,
        avalia_recursos=row_data.avalia_recursos,
        dms_consideracoes_07=row_data.dms_consideracoes_07,
        avalia_gestao=row_data.avalia_gestao,
        dms_consideracoes_08=row_data.dms_consideracoes_08,
        avalia_comunicacao_interna=row_data.avalia_comunicacao_interna,
        avalia_endomarketing=row_data.avalia_endomarketing,
        avalia_treinamentos=row_data.avalia_treinamentos,
        avalia_recrutamento_interno=row_data.avalia_recrutamento_interno,
        avalia_suporte_folhas=row_data.avalia_suporte_folhas,
        avalia_segurança_trabalho=row_data.avalia_segurança_trabalho,
        avalia_canal_ouvidoria=row_data.avalia_canal_ouvidoria,
        avalia_ccq=row_data.avalia_ccq,
        avalia_Onboarding=row_data.avalia_Onboarding,
        dms_consideracoes_09=row_data.dms_consideracoes_09,
        voltaria_para_fgm=row_data.voltaria_para_fgm,
        dms_consideracoes_10=row_data.dms_consideracoes_10,
        indicaria_fgm=row_data.indicaria_fgm,
        dms_consideracoes_11=row_data.dms_consideracoes_11,
        mensagem_fgm=row_data.mensagem_fgm,
        setor = row_data.setor,
        presente_nascimento = row_data.presente_nascimento,
        presente_casamento = row_data.presente_casamento
    )

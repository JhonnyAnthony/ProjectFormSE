import openpyxl
import os

file_name = os.getenv("FILE_NAME")
base_path = os.getenv("BASE_PATH")
class ExcelDataReader:
    def __init__(self, file_name, base_path):
        self.file_name = file_name
        self.base_path = base_path
        self.excel_path = self.update_excel_path()
        self.workbook = openpyxl.load_workbook(self.excel_path)
        self.sheet = self.workbook.active

    def update_excel_path(base_path,file_name):
        return os.path.join(base_path, file_name)

    def get_all_row_data(sheet):
        row_data_list = []
        for row in range(2, sheet.max_row + 1):  # Iterate over all rows.
            if sheet[f'F{row}'].value is not None:  # Check if the name is not null.
                row_data_object = RowData(row, sheet)
                row_data_list.append(row_data_object)
        return row_data_list

# Define the RowData class to hold the data for each row
class RowData:
    def __init__(self, row_idx, sheet):
        self.record_id                          = sheet[f'A{row_idx}'].value
        self.hora_inicio                        = sheet[f'B{row_idx}'].value
        self.hora_conclusao                     = sheet[f'C{row_idx}'].value
        self.email                              = sheet[f'D{row_idx}'].value
        self.nome                               = sheet[f'F{row_idx}'].value
        self.data_admissao                      = sheet[f'G{row_idx}'].value
        self.data_demissao                      = sheet[f'H{row_idx}'].value
        self.setor                              = sheet[f'I{row_idx}'].value
        self.cargo                              = sheet[f'J{row_idx}'].value
        self.iniciativa_desligamento            = sheet[f'K{row_idx}'].value
        self.motivo_desligamento                = sheet[f'L{row_idx}'].value 
        self.avalia_fgm                         = sheet[f'M{row_idx}'].value
        self.dms_consideracoes_01               = sheet[f'N{row_idx}'].value 
        self.avalia_estrutura_fgm               = sheet[f'O{row_idx}'].value
        self.dms_consideracoes_02               = sheet[f'P{row_idx}'].value
        self.avalia_ambiente_fgm                = sheet[f'Q{row_idx}'].value
        self.dms_consideracoes_03               = sheet[f'R{row_idx}'].value
        self.avalia_setor                       = sheet[f'S{row_idx}'].value
        self.dms_consideracoes_04               = sheet[f'T{row_idx}'].value
        self.vale_transporte                    = sheet[f'U{row_idx}'].value
        self.vale_refeicao                      = sheet[f'V{row_idx}'].value
        self.plano_saude_medico                 = sheet[f'W{row_idx}'].value
        self.plano_saude_odontologico           = sheet[f'X{row_idx}'].value
        self.convenio_farmacia                  = sheet[f'Y{row_idx}'].value
        self.convenio_odonto                    = sheet[f'Z{row_idx}'].value
        self.presente_aniversario               = sheet[f'AA{row_idx}'].value
        self.presente_casamento                 = sheet[f'AB{row_idx}'].value
        self.presente_nascimento                = sheet[f'AC{row_idx}'].value
        self.vacina                             = sheet[f'AD{row_idx}'].value
        self.seguro_vida                        = sheet[f'AE{row_idx}'].value
        self.bolsa_estudo                       = sheet[f'AF{row_idx}'].value
        self.dms_consideracoes_05               = sheet[f'AG{row_idx}'].value
        self.avalia_atuacao_cargo               = sheet[f'AH{row_idx}'].value
        self.dms_consideracoes_06               = sheet[f'AI{row_idx}'].value
        self.avalia_recursos                    = sheet[f'AJ{row_idx}'].value
        self.dms_consideracoes_07               = sheet[f'AK{row_idx}'].value
        self.avalia_gestao                      = sheet[f'AL{row_idx}'].value
        self.dms_consideracoes_08               = sheet[f'AM{row_idx}'].value
        self.avalia_comunicacao_interna         = sheet[f'AN{row_idx}'].value
        self.avalia_endomarketing               = sheet[f'AO{row_idx}'].value
        self.avalia_treinamentos                = sheet[f'AP{row_idx}'].value
        self.avalia_recrutamento_interno        = sheet[f'AQ{row_idx}'].value
        self.avalia_suporte_folhas              = sheet[f'AR{row_idx}'].value
        self.avalia_segurança_trabalho          = sheet[f'AS{row_idx}'].value
        self.avalia_canal_ouvidoria             = sheet[f'AT{row_idx}'].value
        self.avalia_ccq                         = sheet[f'AU{row_idx}'].value
        self.avalia_Onboarding                  = sheet[f'AV{row_idx}'].value
        self.dms_consideracoes_09               = sheet[f'AW{row_idx}'].value
        self.voltaria_para_fgm                  = sheet[f'AX{row_idx}'].value
        self.dms_consideracoes_10               = sheet[f'AY{row_idx}'].value
        self.indicaria_fgm                      = sheet[f'AZ{row_idx}'].value
        self.dms_consideracoes_11               = sheet[f'BA{row_idx}'].value
        self.mensagem_fgm                       = sheet[f'BB{row_idx}'].value

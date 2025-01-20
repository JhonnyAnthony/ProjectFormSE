import pandas as pd
from openpyxl import load_workbook

class ExcelDataReader: #Class to declare the variables who get the file path and file name
    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name

    def excel_data(self): # Here get the excel data
        self.df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
        workbook = load_workbook(self.file_path)
        self.sheet = workbook[self.sheet_name]

    def get_excel_row_data(self):
        #Make a array
        row_data_list = []
        # Start on row 2
        for row in range(2, self.sheet.max_row + 1):  # Iterate over all rows.
            # Get the value from column F
            cell_value = self.sheet[f'F{row}'].value
            if cell_value is not None and cell_value.strip():  # Check if the cell is not empty or whitespace.
                row_data_object = RowData(self.sheet, row)
                row_data_list.append(row_data_object)
        return row_data_list

class RowData: # Here declare the variables who will be defined about the row
    def __init__(self, sheet, row_idx): 
        self.nome                               = sheet[f'F{row_idx}'].value
        self.data_demissao                      = sheet[f'G{row_idx}'].value
        self.setor                              = sheet[f'H{row_idx}'].value
        self.cargo                              = sheet[f'I{row_idx}'].value
        self.iniciativa_desligamento            = sheet[f'J{row_idx}'].value
        self.motivodesliga                      = sheet[f'K{row_idx}'].value 
        self.avaliacaojornada                   = sheet[f'L{row_idx}'].value
        self.dms_consideracoes_01               = sheet[f'M{row_idx}'].value 
        self.beneficios                         = sheet[f'N{row_idx}'].value
        self.beneficiostxt                      = sheet[f'O{row_idx}'].value
        self.avalia_ambiente_fgm                = sheet[f'P{row_idx}'].value
        self.dms_consideracoes_04               = sheet[f'Q{row_idx}'].value
        self.mudancastrab                       = sheet[f'R{row_idx}'].value
        self.comunicacao                        = sheet[f'S{row_idx}'].value
        self.comunicatxt                        = sheet[f'T{row_idx}'].value
        self.treinamentos                       = sheet[f'U{row_idx}'].value
        self.oportunidades                      = sheet[f'V{row_idx}'].value
        self.orientacao                         = sheet[f'W{row_idx}'].value
        self.consilideranca                     = sheet[f'X{row_idx}'].value
        self.feedback                           = sheet[f'Y{row_idx}'].value
        self.gestao                             = sheet[f'Z{row_idx}'].value
        self.indicaria_fgm                      = sheet[f'AA{row_idx}'].value
        self.recomendatxt                       = sheet[f'AB{row_idx}'].value
        self.mensagemparafgm                    = sheet[f'AC{row_idx}'].value



        # self.avalia_estrutura_fgm               = sheet[f'O{row_idx}'].value
        # self.dms_consideracoes_02               = sheet[f'P{row_idx}'].value
        # self.avalia_setor                       = sheet[f'S{row_idx}'].value
        # self.dms_consideracoes_04               = sheet[f'T{row_idx}'].value
        # self.vale_transporte                    = sheet[f'U{row_idx}'].value
        # self.vale_refeicao                      = sheet[f'V{row_idx}'].value
        # self.plano_saude_medico                 = sheet[f'W{row_idx}'].value
        # self.plano_saude_odontologico           = sheet[f'X{row_idx}'].value
        # self.convenio_farmacia                  = sheet[f'Y{row_idx}'].value
        # self.convenio_odonto                    = sheet[f'Z{row_idx}'].value
        # self.presente_aniversario               = sheet[f'AA{row_idx}'].value
        # self.presente_casamento                 = sheet[f'AB{row_idx}'].value
        # self.presente_nascimento                = sheet[f'AC{row_idx}'].value
        # self.vacina                             = sheet[f'AD{row_idx}'].value
        # self.seguro_vida                        = sheet[f'AE{row_idx}'].value
        # self.bolsa_estudo                       = sheet[f'AF{row_idx}'].value
        # self.dms_consideracoes_05               = sheet[f'AG{row_idx}'].value
        # self.avalia_atuacao_cargo               = sheet[f'AH{row_idx}'].value
        # self.dms_consideracoes_06               = sheet[f'AI{row_idx}'].value
        # self.avalia_recursos                    = sheet[f'AJ{row_idx}'].value
        # self.dms_consideracoes_07               = sheet[f'AK{row_idx}'].value
        # self.avalia_gestao                      = sheet[f'AL{row_idx}'].value
        # self.dms_consideracoes_08               = sheet[f'AM{row_idx}'].value
        # self.avalia_endomarketing               = sheet[f'AO{row_idx}'].value
        # self.avalia_treinamentos                = sheet[f'AP{row_idx}'].value
        # self.avalia_recrutamento_interno        = sheet[f'AQ{row_idx}'].value
        # self.avalia_suporte_folhas              = sheet[f'AR{row_idx}'].value
        # self.avalia_segurança_trabalho          = sheet[f'AS{row_idx}'].value
        # self.avalia_canal_ouvidoria             = sheet[f'AT{row_idx}'].value
        # self.avalia_ccq                         = sheet[f'AU{row_idx}'].value
        # self.avalia_Onboarding                  = sheet[f'AV{row_idx}'].value
        # self.dms_consideracoes_09               = sheet[f'AW{row_idx}'].value
        # self.voltaria_para_fgm                  = sheet[f'AX{row_idx}'].value
        # self.dms_consideracoes_10               = sheet[f'AY{row_idx}'].value
        
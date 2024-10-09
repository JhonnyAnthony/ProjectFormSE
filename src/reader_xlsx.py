import openpyxl
import pandas as pd
import os


# variavel que localiza o arquivo excel
def find_excel():
    base_path = r'C:\Users\jhonny.souza\Downloads'
    return os.path.join(base_path)

#define o onde o arquivo está
excel_path = find_excel('Entrevista Maio.xlsx')

# Carregar os dados da planilha do Excel
df = pd.read_excel(excel_path, skiprows=2)
workbook = openpyxl.load_workbook(excel_path)
# Obter a primeira planilha
sheet = workbook.active
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
            dms_consideracoes_1                     = sheet[f'BA{row_idx}'].value
            mensagem_fgm                            = sheet[f'BB{row_idx}'].value

            # Print the values
            print(f"mensagem: {id}")
# retorna a variavel para a execução
responses_variable()

import openpyxl
import pandas as pd
import os

def update_excel_path(new_file_name):
    base_path = r'C:\Users\jhonny.souza\Downloads'
    return os.path.join(base_path, new_file_name)

# Inicialmente, defina o caminho do arquivo
excel_path = update_excel_path('Entrevista de Desligamento.xlsx')

# Carregar a planilha do Excel
df = pd.read_excel(excel_path)

workbook = openpyxl.load_workbook(excel_path)

# Obter a primeira planilha
sheet = workbook.active

# Ler dados de células específicas (por exemplo, A1)
cell_value = sheet['A1'].value

print(cell_value)

# Exemplo de atualização do caminho do arquivo


# Carregar a nova planilha do Excel
df = pd.read_excel(excel_path)

workbook = openpyxl.load_workbook(excel_path)

# Obter a primeira planilha do novo arquivo
sheet = workbook.active

# Ler dados de células específicas do novo arquivo (por exemplo, A1)
cell_value = sheet['A1'].value

print(df)

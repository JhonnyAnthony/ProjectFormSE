from reader_xlsx import ExcelDataReader


# Usage
base_path = r'C:\\Users\\jhonny.souza\\Downloads'
file_name = 'Entrevista Maio.xlsx'
reader = ExcelDataReader(file_name, base_path)
all_row_data = reader.get_all_row_data()

# Now you can use all_row_data in your main code
for row_data in all_row_data:
    print(row_data.id)
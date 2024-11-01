import pyodbc
import logging

class DatabaseDataReader:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def load_database(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            logging.info("Connection successful!")
            self.cursor = self.conn.cursor()
        except Exception as e:
            logging.error(f"Error: {e}")
            if self.conn:
                self.conn.close()
    #Here get data about dataadmiss, datademiss,idprocess
    def get_se_row_data(self):
        row_data_list = []
        try:
            self.cursor.execute("""
                                SELECT
                                    T0.NOMCOL AS NOMECOLABORADOR,
                                    T0.DATAADMISS  AS DATAADMISS,
                                    T0.DATADEMISS AS DATADEMISS,
                                    WFP.IDPROCESS AS IDPROCESS
                                FROM
                                    DYNDLC02 T0
                                INNER JOIN
                                    GNASSOCFORMREG FORMREG
                                    ON FORMREG.OIDENTITYREG = T0.OID
                                INNER JOIN
                                    WFPROCESS WFP
                                    ON FORMREG.CDASSOC = WFP.CDASSOCREG
                                WHERE
                                    WFP.CDPROCESSMODEL = '2518';
                                """) # 2518 = qas
                                     # 2550 = prd
            rows = self.cursor.fetchall()
            for row in rows:
                row_data_object = RowData(row)
                row_data_list.append(row_data_object)
        except Exception as e:
            logging.error(f"Error: {e}  - Conection")
        finally:
            self.cursor.close()
            self.conn.close()
        return row_data_list

class RowData: #Declare the variables to be called
    def __init__(self, row):
        self.nome_colaborador = row.NOMECOLABORADOR
        self.data_admissao = row.DATAADMISS
        self.data_demissao = row.DATADEMISS
        self.id_process = row.IDPROCESS

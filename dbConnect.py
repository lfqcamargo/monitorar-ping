from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

load_dotenv()

class DataBaseConnection:
    def __init__(self):
        """Inicializa a conexão com o banco de dados MySQL usando variáveis de ambiente."""
        self.connection = None
        self.connect()

    def connect(self):
        """Estabelece uma conexão com o banco de dados MySQL usando variáveis de ambiente."""
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(
                    host=os.getenv('DB_HOST', 'localhost'),
                    database=os.getenv('DB_NAME'),
                    user=os.getenv('DB_USER'),
                    password=os.getenv('DB_PASSWORD')
                )
                if self.connection.is_connected():
                    db_info = self.connection.get_server_info()
                    print(f"Conectado ao servidor MySQL versão {db_info}")
            except Error as e:
                print(f"Erro ao conectar ao MySQL: {e}")

    def inserir(self, tempo, site, data_hora):
        """Insere um registro no banco de dados."""
        insert_query = """
        INSERT INTO ping (PING_VAL_MEDIO, PING_NOME, PING_DAT)
        VALUES (%s, %s, %s);
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(insert_query, (tempo, site, data_hora))
            self.connection.commit()
            print(f"Registro inserido com sucesso: {tempo}, {site}, {data_hora}")
        except Error as e:
            print(f"Erro ao inserir registro no banco de dados: {e}")
        finally:
            cursor.close()

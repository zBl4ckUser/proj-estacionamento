import sqlite3 as db
import os

class Colors :
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' # Tira a cor
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

table = ["Cliente","Registro","Funcionario", "CadastroCliente"]
columns = ["cpf, placa, tipo_auto", "idCliente, entrada, saida, preco", "nome, cpf, rg, telefone, endereco, salario"\
           ,"nome, cpf, telefone"
           ]

def get_documents_folder():
    if os.name == 'nt':  # Windows / Não foi testado
        from pathlib import Path
        documents_folder = str(Path.home() / 'Documents')
    else:  # Linux
        documents_folder = os.path.expanduser('~/Documents')
    
    estaciona_plus_folder = os.path.join(documents_folder, 'estaciona+')
    if not os.path.exists(estaciona_plus_folder):
        os.makedirs(estaciona_plus_folder)
    
    return estaciona_plus_folder

def create_database_if_not_exists(db_path, sql_script_path):
    if not os.path.exists(db_path):
        print(f"{Colors.OKBLUE}[INFO]{db_path} não encontrado. Criando novo banco de dados.{Colors.ENDC}")
        conn = db.connect(db_path)
        cursor = conn.cursor()
        with open(sql_script_path, 'r') as sql_file:
            sql_script = sql_file.read()
        cursor.executescript(sql_script)
        conn.commit()
        conn.close()
        print(f"{Colors.OKBLUE}[INFO]Banco de dados criado e instruções SQL executadas.{Colors.ENDC}")

def connect_to_db() -> bool:
    documents_folder = get_documents_folder()
    db_path = os.path.join(documents_folder, 'estacionamento.db')
    sql_script_path = 'database/tables.sql'
    create_database_if_not_exists(db_path, sql_script_path)

    try:
        global connection
        connection = db.connect(db_path)
        print(f"{Colors.OKGREEN}[DB]: Conexão com banco de dados realizada com sucesso{Colors.ENDC}")
        return True
    except Exception as err:
        print(f"{Colors.FAIL}[DB]: Conexão não pôde ser realizada{Colors.ENDC}")
        print(f"{Colors.WARNING}Erro: {err}{Colors.ENDC}")
        return False
    
def insert_into_db(table, columns, values):
        cursor = connection.cursor()
        sComando = f"Insert into {table}" +\
                    f"({columns})" +\
                    f" values ({values})"
        try:
            cursor.execute(sComando)
            connection.commit()
            return True
        except db.Error as err:
            print(f"{Colors.FAIL}[BD] Inserção no banco de dados falhou!{Colors.ENDC}")
            print(f"{Colors.WARNING}Error is: {err.args[0]}{Colors.ENDC}")
            cursor.close()
            return False

def get_client_id():
        cursor = connection.cursor()
        sSelect = f"select max(idCliente) from Cliente"
        result = cursor.execute(sSelect)
        id = result.fetchone()
        cursor.close()
        return id[0]

def db_form():
            connect_to_db()

def verify_premium():
    cursor = connection.cursor()
    sVerify = "UPDATE Cliente\
    SET premium = (\
        SELECT CASE\
            WHEN EXISTS (\
                SELECT 1\
                FROM CadastroCliente\
                WHERE CadastroCliente.cpf = Cliente.cpf\
            ) THEN 1\
            ELSE 0\
        END\
    )\
    "
    cursor.execute(sVerify)
    connection.commit()
    cursor.close()

def verify_if_registry_exist(reg: int) -> bool:
    cursor = connection.cursor()
    sVerify = f"SELECT * FROM Registro r where r.idRegistro = {reg}"
    result = cursor.execute(sVerify)
    if result.fetchone() is None:
        cursor.close()
        return False
    else:
        cursor.close()
        return True

def verify_if_employee_exist(reg: int) -> bool:
    cursor = connection.cursor()
    sVerify = f"SELECT * FROM Funcionario f WHERE f.idFuncionario = {reg}"
    result = cursor.execute(sVerify)
    if result.fetchone() is None:
        cursor.close()
        return False
    else:
        cursor.close()
        return True
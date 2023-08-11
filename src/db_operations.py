from DBDialog import FormDB
from pwd_treat import decrypt_password, crypt_password
import pyodbc as db
import os
from PySide6 import QtWidgets


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
columns = ["cpf, placa, tipo_auto", "idCliente, entrada, saida", "nome, cpf, rg, telefone, endereco, salario"\
           ,"nome, cpf, telefone"
           ]


def find_drivers():
    installed_drivers = db.drivers()

    # Verifica se há drivers instalados
    if installed_drivers:
        return installed_drivers[0]
    else:
        raise Exception("Nenhum driver ODBC encontrado no sistema.")

def check_os():
    import platform
    if platform.system() == "Linux":
        return find_drivers()
    elif platform.system() == "Windows":
        return find_drivers()

def connect_to_db(pwd, user, server, database) -> bool:
        try: 
            global connection
            connection = db.connect(
                                driver=check_os(),
                                server=f"{server}",
                                database=f"{database}",
                                uid=f"{user}",
                                pwd=f"{pwd}",
                                TrustServerCertificate='yes'
                                )
            print(f"{Colors.OKGREEN}[DB]: Conexão com banco de dados realizada com sucesso{Colors.ENDC}")
            return True
        except Exception as err:
            print(f"{Colors.FAIL}[DB]: Conexão não pôde ser realizada{Colors.ENDC}")
            print(f"Erro: {err}")
            return False



def insert_into_db(table, columns, values):
        cursor = connection.cursor()
        sComando = f"Insert into Estacionamento.{table}" +\
                    f"({columns})" +\
                    f" values ({values})"
        try:
            cursor.execute(sComando)
        except db.Error as err:
            print(f"{Colors.FAIL}[BD] Inserção no banco de dados falhou!{Colors.ENDC}")
            print(f"Error is: {err.args[1]}")
        cursor.commit()
        cursor.close()

def get_client_id():
        cursor = connection.cursor()
        sSelect = f"select max(idCliente) from Estacionamento.Cliente"
        result = cursor.execute(sSelect)
        id = result.fetchone()
        cursor.close()
        return id[0]

def db_form():
        global pwd, user, server, database
        if os.path.isfile("./db.txt"):
            arquivo = open("./db.txt", "rb")

            encrypted_pwd = arquivo.readline().strip()
            user = bytes(arquivo.readline().strip()).decode("utf-8")
            server = bytes(arquivo.readline().strip()).decode("utf-8")
            database = bytes(arquivo.readline().strip()).decode("utf-8")

            pwd_decrypted = decrypt_password(encrypted_pwd)
            connect_to_db(pwd_decrypted, user, server, database)
            
            arquivo.close()
        else:        
            dialog = FormDB()
            dialog.exec()
            pwd = dialog.ed_pwd.text()
            user = dialog.ed_user.text()
            server = dialog.ed_server.text()
            database = dialog.ed_db.text()
            arquivo = open("db.txt", "ab") # abre o arquivo em modo 'append binary'

            pwd_hash = crypt_password(pwd)
            
            # Salva na seguinte ordem: Senha - usuário - servidor - database
            file_content = pwd_hash  + b"\n" + user.encode("utf-8") + b"\n" +server.encode("utf-8")  + b"\n" + database.encode("utf-8")
            arquivo.write(file_content)
            arquivo.close()

            connect_to_db(pwd, user, server, database)

def verify_premium():
    cursor = connection.cursor()
    sVerify = "UPDATE Estacionamento.Cliente\
        SET premium = CASE\
            WHEN Estacionamento.Cliente.cpf = Estacionamento.CadastroCliente.cpf THEN 1\
            ELSE 0\
            END\
        FROM Estacionamento.Cliente\
        INNER JOIN Estacionamento.CadastroCliente ON Estacionamento.Cliente.cpf = Estacionamento.CadastroCliente.cpf"
    cursor.execute(sVerify)
    cursor.close()

def verify_if_registry_exist(reg: int) -> bool:
    cursor = connection.cursor()
    sVerify = f"SELECT * FROM Estacionamento.Registro r where r.idRegistro = {reg}"
    result = cursor.execute(sVerify)
    if result.fetchone() is None:
        cursor.close()
        return False
    else:
        cursor.close()
        return True

def verify_if_employee_exist(reg: any) -> bool:
    cursor = connection.cursor()
    sVerify = f"SELECT * FROM Estacionamento.Funcionario f WHERE f.idFuncionario = {reg}"
    result = cursor.execute(sVerify)
    if result.fetchone() is None:
        cursor.close()
        return False
    else:
        cursor.close()
        return True
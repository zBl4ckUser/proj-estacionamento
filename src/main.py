from PySide6.QtWidgets import QApplication
from FormPrincipal import Colors, FormPrincipal

def handle_close():
    from db_operations import connection
    connection.close()
    print(f"{Colors.OKGREEN}[DB]: Conexão com o banco de dados fechada {Colors.ENDC}")
    

if __name__ == "__main__":
    aplicacao = QApplication()
    janela = FormPrincipal()
    aplicacao.aboutToQuit.connect(handle_close)
    aplicacao.exec()
    


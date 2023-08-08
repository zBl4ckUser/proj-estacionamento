#QT FILES
from UI_Estacionamento_ui import Ui_MainWindow
#QT UTIL
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QDateTime
#UTILS
import datetime
import re
from db_operations import insert_into_db, get_client_id, db_form, verify_premium, \
    table, columns, verify_if_registry_exist

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' # Tira a cor
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class FormPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        db_form() 

        self.dtEntrada.setDateTime(datetime.datetime.now())
        self.dtSaida.setDateTime(datetime.datetime.now())

        self.actionCadastrar_Cliente.triggered.connect(self.t_cadastrar_cliente)
        self.actionCadastrar_Funcionario.triggered.connect(self.t_cadastrar_func)
        self.actionListar.triggered.connect(self.t_listar)
        self.actionNovo_Registro.triggered.connect(self.t_novo_registro)
        self.actionAdmin.triggered.connect(self.t_admin)
        self.btnCriar_Reg.clicked.connect(self.new_reg)
        self.btnCad_Func.clicked.connect(self.new_func)
        self.btnCancelar.clicked.connect(self.cancel)
        self.btnCan_Func.clicked.connect(self.cancel)
        self.btnCad_Cli.clicked.connect(self.new_cad_client)
        self.btnAlterar.clicked.connect(self.change_price)
        self.btnDeletar.clicked.connect(self.delete_reg)
        self.btnRem_Func.clicked.connect(self.remove_func)

        int_validator = QIntValidator()
        self.edReg_ID.setValidator(int_validator)

        current_dt = QDateTime.currentDateTime()
        self.dtEntrada.setMinimumDateTime(current_dt)
        self.dtSaida.setMinimumDateTime(current_dt)

        self.spbCarro.setValue(3)
        self.spbMoto.setValue(2)
        self.dspbDesconto.setValue(0.50)

        self.preco_carro = self.spbCarro.value()
        self.preco_moto = self.spbMoto.value()
        self.desconto = self.dspbDesconto.value()

        self.tabWidget.currentChanged.connect(self.on_tab_change)

    def warning_msg(self, title = "Informações faltantes", message ="Insira todos os valores necessários!"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    # T de Tool
    def t_cadastrar_cliente(self):
        self.tabWidget.show()
        self.next_tab(3)

    def t_cadastrar_func(self):
        self.tabWidget.show()
        self.next_tab(4)
    
    def t_listar(self):
        self.tabWidget.show()
        if self.tabWidget.currentIndex() == 1:
            self.next_tab(2)
        else:
            self.next_tab(1)

    def t_novo_registro(self):
        self.tabWidget.show()
        self.next_tab(0)

    def t_admin(self):
        self.tabWidget.hide()

    def t_admin(self):
        self.next_tab(5)
        
    def change_price(self):
        self.preco_carro = self.spbCarro.value()
        self.preco_moto = self.spbMoto.value()
        self.desconto = self.dspbDesconto.value()

    def delete_reg(self):
        from db_operations import connection
        cursor = connection.cursor()
        
        if self.edReg_ID.text() == '':
            print(f"{Colors.FAIL}Nenhum registro foi informado{Colors.ENDC}")
            self.warning_msg("Informação faltante","Nenhum registro foi informado")
        else:
            reg_id = int(self.edReg_ID.text())
            sDel = f"DELETE FROM Estacionamento.Registro WHERE idRegistro = {reg_id}"
            if verify_if_registry_exist(reg_id):
                try:
                    cursor.execute(sDel)
                    print(f"{Colors.OKGREEN} Registro {reg_id} deletado")
                    cursor.commit() # SALVA AS MUDANÇAS FEITAS NO BANCO DE DADOS
                except Exception as err:
                    print(f"{Colors.FAIL}Erro ao deletar registro!{Colors.ENDC}")
                    print(f"Erro: {err}")
            else:
                print(f"{Colors.FAIL}O Registro não existe{Colors.ENDC}")
                self.warning_msg("Erro!", "O Registro não existe")
            cursor.close()

    def remove_func(self):
        from db_operations import connection
        try:
            func_id = int(self.edFunc_ID.text())
            sDel = f"DELETE FROM Estacionamento.Funcionario WHERE idFuncionario = {func_id}"
        except:
            func_id = self.edFunc_ID.text()
            sDel = f"DELETE FROM Estacionamento.Funcionario WHERE nome = '{func_id}'"
        cursor = connection.cursor()
        # ?????????????????
        
        try:
            cursor.execute(sDel)
            print(f"{Colors.OKGREEN}Registro {func_id} deletado")
        except Exception as err:
            print(f"{Colors.FAIL}Erro ao deletar registro!{Colors.ENDC}")
            print(f"Erro: {err}")

        cursor.commit() # SALVA AS MUDANÇAS FEITAS NO BANCO DE DADOS
        cursor.close()

    def clear_inputs(self):
        self.edReg_ID.clear()
        self.edFunc_ID.clear()
        self.edCPF.clear()
        self.edPlaca.clear()
        self.dtEntrada.setDateTime(datetime.datetime.now())
        self.dtSaida.setDateTime(datetime.datetime.now())
    
        self.edNome_Func.clear()
        self.edCPF_Func.clear()
        self.edRG_Func.clear()
        self.etEndereco.clear()
        self.edTel_Func.clear()
        self.edSalario.clear()
    
        self.edNome_Cliente.clear()
        self.edCPF_Cli.clear()
        self.edTel_Cliente.clear()
        
    def new_reg(self):
        regex_placa = r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$' # regex de validação para placa

        if self.edCPF.text() == "   .   .   -  " or self.edPlaca.text() == "-" :
            self.warning_msg()
        if  not re.match(regex_placa, self.edPlaca.text().replace("-", "")): # FAZ A VALIDAÇÃO REGEX
            self.warning_msg("Placa Inválida", "A Placa inserida é inválida")
            print(f"{Colors.FAIL}A Placa inserida é inválida{Colors.ENDC}")
        else:
            placa = self.edPlaca.text()
            print(f"{Colors.OKGREEN} A Placa inserida é válida{Colors.ENDC}")
            client_cpf = self.edCPF.text() 
            entry_date = self.dtEntrada.text()
            departure_time = self.dtSaida.text()
            type_auto = self.cbxTipo.currentText()
            client_insert = f"'{client_cpf}', '{placa}', '{type_auto}'"
            
            insert_into_db(table[0], columns[0], client_insert) # Novo Cliente
            verify_premium() # verifica se o cliente já é cadastrado 

            client_id = get_client_id()  
            registry_insert = f"{client_id}, CONVERT(DATETIME, '{entry_date}'), CONVERT(DATETIME, '{departure_time}')"
            
            insert_into_db(table[1], columns[1], registry_insert) # Novo registro

            self.clear_inputs()

    def new_func(self):

        if self.edCPF_Func.text() == "   .   .   -  " or self.edNome_Func.text() == "" or\
           self.edRG_Func.text() == "  .   .   - " or self.edSalario.text() == ""\
           or self.edTel_Func.text()== "(  )    -     " or self.etEndereco.toPlainText() == "":
            self.warning_msg()
        else:
            nome_func = self.edNome_Func.text()
            cpf_func  = self.edCPF_Func.text()
            rg_func   = self.edRG_Func.text()
            endereco  = self.etEndereco.toPlainText()
            tel_func  = self.edTel_Func.text()
            salario   = self.edSalario.text()
        
            values = f"'{nome_func}', '{cpf_func}', '{rg_func}', '{tel_func}', '{endereco}', CONVERT(MONEY, '{salario}')"

            insert_into_db(table[2], columns[2], values)

            self.clear_inputs()

    def new_cad_client(self):
        if self.edCPF_Cli.text() == "   .   .   -  " or self.edNome_Cliente.text() == "" or  self.edTel_Cliente.text() == "(  )    -     ":
            self.warning_msg()
        else:
            cli_name = self.edNome_Cliente.text()
            cli_cpf = self.edCPF_Cli.text()
            if self.verify_if_cad_exist(str(cli_cpf)):
                self.warning_msg("Cadastro já existe", "Já existe alguém cadastrado com esse CPF")
            else:
                cli_tel = self.edTel_Cliente.text()
                values = f"'{cli_name}', '{cli_cpf}', '{cli_tel}'"
                insert_into_db(table[3], columns[3], values)

            self.clear_inputs()

    def list_reg(self):
        from db_operations import connection
        self.twReg.clearContents()  # Limpa os conteúdos das células
        self.twReg.setRowCount(0)  # Define o número de linhas como zero

        cursor = connection.cursor()

        sFunc = f"SELECT\
            Estacionamento.Cliente.idCliente,\
            CASE\
                WHEN Estacionamento.Cliente.premium = 1 THEN Estacionamento.CadastroCliente.nome\
                ELSE ''\
            END AS nome,\
            Estacionamento.Cliente.placa,\
            Estacionamento.Registro.entrada,\
            Estacionamento.Registro.saida,\
            CASE\
                WHEN Estacionamento.Cliente.tipo_auto = 'carro' THEN DATEDIFF(hour, Estacionamento.Registro.entrada, Estacionamento.Registro.saida) * {self.preco_carro}\
                WHEN Estacionamento.Cliente.tipo_auto = 'moto' THEN DATEDIFF(hour, Estacionamento.Registro.entrada, Estacionamento.Registro.saida) * {self.preco_moto}\
            END * CASE WHEN Estacionamento.Cliente.premium = 1 THEN {self.desconto} ELSE 1 END AS valor\
            FROM\
            Estacionamento.Cliente\
            LEFT JOIN Estacionamento.CadastroCliente ON Estacionamento.Cliente.cpf = Estacionamento.CadastroCliente.cpf\
            INNER JOIN Estacionamento.Registro ON Estacionamento.Cliente.idCliente = Estacionamento.Registro.idCliente\
            "
        cursor.execute(sFunc)
        result = cursor.fetchall()

        for row_number, row_data in enumerate(result):
            self.twReg.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.twReg.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        cursor.close()

    def verify_if_cad_exist(self, cpf) -> bool : 
        from db_operations import connection
        cursor = connection.cursor()
        sCommand = f"select * from Estacionamento.CadastroCliente where cpf = '{cpf}'"
        result = cursor.execute(sCommand)
        if result.fetchone() is None:
            cursor.close()
            return False
        else:
            cursor.close()
            return True
        

    def list_func(self):
        self.twFunc.clearContents()  # Limpa os conteúdos das células
        self.twFunc.setRowCount(0)  # Define o número de linhas como zero
        
        from db_operations import connection

        cursor = connection.cursor()
        sFunc = "SELECT * FROM Estacionamento.Funcionario"
        result = cursor.execute(sFunc)

        for row_number, row_data in enumerate(result):
            self.twFunc.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.twFunc.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        cursor.close()

    def on_tab_change(self, index):
        
        if index == 1:
            self.list_reg()
        if index == 2:
            self.list_func()

    def cancel(self):
        self.clear_inputs()

    def next_tab(self, index):
        self.tabWidget.setCurrentIndex(index)
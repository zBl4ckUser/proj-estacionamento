CREATE TABLE Cliente (
    idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT NOT NULL,
    placa TEXT NOT NULL,
    tipo_auto TEXT DEFAULT 'Carro',
    premium INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE Registro (
    idRegistro INTEGER PRIMARY KEY AUTOINCREMENT,
    idCliente INTEGER NOT NULL,
    entrada DATETIME NOT NULL,
    saida DATETIME NULL,
    preco REAL NULL DEFAULT 0,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
);

CREATE TABLE Funcionario (
    idFuncionario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    rg TEXT NOT NULL,
    telefone TEXT NOT NULL,
    endereco TEXT NOT NULL,
    salario REAL NOT NULL
);

CREATE TABLE CadastroCliente (
    idCadastroCliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    telefone TEXT NOT NULL
);
create schema Estacionamento

create table Estacionamento.Cliente(
	idCliente int identity primary key,
	cpf varchar(14) not null,
	placa varchar(8) not null,
	tipo_auto varchar(5) default 'Carro',
	premium bit not null default 0
)

create table Estacionamento.Registro(
	idRegistro int identity primary key,
	idCliente int not null,
	entrada datetime not null,
	saida datetime null,
	constraint fk_idCliente foreign key(idCliente)
	references Estacionamento.Cliente(idCliente)
)

create table Estacionamento.Funcionario(
	idFuncionario int identity primary key,
	nome varchar(40) not null,
	cpf varchar(14) not null,
	rg varchar(12) not null,
	telefone varchar(14) not null,
	endereco text not null,
	salario money not null
)


/*
 * Verifica se o cpf do cliente já está cadastrado;
 * Se estiver, muda a situação de cadastro (que é o 'premium')
 * para verdadeiro
*/
UPDATE Estacionamento.Cliente
SET premium = CASE
    WHEN Estacionamento.Cliente.cpf = Estacionamento.CadastroCliente.cpf THEN 1
    ELSE 0
    END
FROM Estacionamento.Cliente
INNER JOIN Estacionamento.CadastroCliente ON Estacionamento.Cliente.cpf = Estacionamento.CadastroCliente.cpf	



select * from Estacionamento.Cliente
select * from Estacionamento.Registro
select * from Estacionamento.Funcionario
select * from Estacionamento.CadastroCliente 

delete from Estacionamento.Registro 
delete from Estacionamento.CadastroCliente 
delete from Estacionamento.Cliente 
delete from Estacionamento.Funcionario 

DBCC CHECKIDENT ('Estacionamento.Cliente', RESEED, 0)
DBCC CHECKIDENT ('Estacionamento.Registro', RESEED, 0)
DBCC CHECKIDENT ('Estacionamento.Funcionario', RESEED, 0)
DBCC CHECKIDENT ('Estacionamento.CadastroCliente', RESEED, 0)

create table Estacionamento.CadastroCliente(
	idCadastroCliente int identity primary key,
	nome varchar(40) not null,
	cpf varchar(14) not null,
	telefone varchar(14) not null
)


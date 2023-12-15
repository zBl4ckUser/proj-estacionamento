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
	preco money null default 0,
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

create table Estacionamento.CadastroCliente(
	idCadastroCliente int identity primary key,
	nome varchar(40) not null,
	cpf varchar(14) not null,
	telefone varchar(14) not null
)

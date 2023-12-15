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

/*
 * Verifica se o cpf do cliente já está cadastrado;
 * Se estiver, muda a situação de cadastro (que é o 'premium')
 * para verdadeiro
*/
UPDATE Cliente
SET premium = CASE
    WHEN Cliente.cpf = CadastroCliente.cpf THEN 1
    ELSE 0
    END
FROM Cliente
INNER JOIN CadastroCliente ON Cliente.cpf = CadastroCliente.cpf	



select * from Cliente
select * from Registro
select * from Funcionario
select * from CadastroCliente 

delete from Registro 
delete from CadastroCliente 
delete from Cliente 
delete from Funcionario 

DBCC CHECKIDENT ('Cliente', RESEED, 0)
DBCC CHECKIDENT ('Registro', RESEED, 0)
DBCC CHECKIDENT ('Funcionario', RESEED, 0)
DBCC CHECKIDENT ('CadastroCliente', RESEED, 0)

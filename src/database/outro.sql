create trigger tr_isPremium on Estacionamento.Cliente
for insert
as 
begin 
    set nocount on;
    declare @cliente_cpf varchar(14)
    select @cliente_cpf = cpf from inserted 
    update Estacionamento.Cliente set premium = CASE
    WHEN Estacionamento.Cliente.cpf = Estacionamento.CadastroCliente.cpf THEN 1
    ELSE 0
    END
    FROM Estacionamento.Cliente
    INNER JOIN Estacionamento.CadastroCliente ON Estacionamento.Cliente.cpf = Estacionamento.CadastroCliente.cpf	
end

create trigger tr_isPremium on Cliente
for insert
as 
begin 
    set nocount on;
    declare @cliente_cpf varchar(14)
    select @cliente_cpf = cpf from inserted 
    update Cliente set premium = CASE
    WHEN Cliente.cpf = CadastroCliente.cpf THEN 1
    ELSE 0
    END
    FROM Cliente
    INNER JOIN CadastroCliente ON Cliente.cpf = CadastroCliente.cpf	
end

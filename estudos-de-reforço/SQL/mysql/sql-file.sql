SELECT * FROM categorias;
SELECT * FROM clientes;
SELECT * FROM locais;
SELECT * FROM lojas;
SELECT * FROM pedidos;
SELECT * FROM produtos;

SELECT -- Quantidade de pessoas de cada sexo
	Sexo,
    COUNT(Sexo) AS 'Qtd. Pessoas'
FROM clientes
GROUP BY Sexo;

SELECT -- Todas as clientes mulheres do BD
	ID_Cliente,
	Nome, 
    Sobrenome,
    Data_Nascimento,
    Estado_Civil AS 'Estado Civil',
	Sexo,
    Telefone,
    Qtd_filhos AS 'Quantidade de Filhos',
    Escolaridade AS 'Grau de Escolaridade'
FROM clientes
WHERE Sexo = 'F' and Estado_Civil = 'S'
ORDER BY Qtd_Filhos ASC;

-- INNER JOIN

SELECT -- (INNER JOIN) juntando tabelas...
	pedidos.ID_Pedido AS 'ID PEDIDO',
    pedidos.ID_Cliente AS 'ID CLIENTE',
	pedidos.ID_Produto AS 'ID PRODUTO',
    pedidos.Data_Venda AS 'DATA DE VENDA',
    pedidos.Qtd_Vendida AS 'QUANTIDADE VENDIDA',
    pedidos.Receita_Venda AS 'RECEITA VENDA',
    pedidos.Custo_Venda AS 'CUSTO VENDA',
    pedidos.Custo_Unit AS 'CUSTO UNITÁRIO',
    pedidos.Preco_Unit AS 'PREÇO UNITÁRIO',
    pedidos.ID_Loja AS 'ID DA LOJA',
    lojas.Gerente AS 'GERENTE',
    lojas.Telefone AS 'TELEFONE',
    lojas.Loja AS 'LOJA'
    
FROM pedidos
INNER JOIN lojas
	ON pedidos.ID_Loja = lojas.ID_Loja
ORDER BY lojas.ID_Loja;

	
SELECT -- quanto cada gerente faturou em cada loja organizada pelo maior faturamento até o menor faturamento
	pedidos.ID_Loja,
	lojas.Gerente,
    lojas.Loja,
    COUNT(pedidos.Preco_Unit) AS 'Qtd. Vendas',
    SUM(pedidos.Preco_Unit) AS 'Faturamento'
FROM pedidos
INNER JOIN Lojas
	ON pedidos.ID_Loja = lojas.ID_Loja
GROUP BY pedidos.ID_Loja, lojas.Gerente, lojas.Loja
ORDER BY 'Faturamento';


SELECT
	pedidos.ID_Cliente,
    pedidos.ID_Loja,
    pedidos.ID_Produto,
    produtos.Nome_Produto,
    produtos.Marca_Produto,
    lojas.Loja,
    lojas.Gerente,
    lojas.Telefone
FROM pedidos
INNER JOIN lojas
	ON pedidos.ID_loja = lojas.ID_Loja
    
INNER JOIN produtos
	ON pedidos.ID_Produto = produtos.ID_Produto
    
ORDER BY ID_Loja;
	









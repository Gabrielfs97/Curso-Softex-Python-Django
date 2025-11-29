-- Active: 1764452542036@@127.0.0.1@3306
CREATE TABLE Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL,                  
    email TEXT UNIQUE NOT NULL          
);

CREATE TABLE Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT,
    preco REAL,                          
    estoque INTEGER                     
);

CREATE TABLE Pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    data_compra DATETIME DEFAULT CURRENT_TIMESTAMP, 
    total REAL,                           
    id_cliente INTEGER,                   
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
);

CREATE TABLE Itens_Pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    id_pedido INTEGER,                   
    id_produto INTEGER,                   
    quantidade INTEGER,                   
   
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id)
);

INSERT INTO Clientes (nome, email) VALUES
('João', 'joao.silva@email.com'),
('Maria', 'maria.souza@email.com'),
('Ana', 'ana.oliveira@email.com');

INSERT INTO Produtos (nome, preco, estoque) VALUES
('Teclado Mecânico RGB', 350.00, 50),
('Mouse Sem Fio Ergonômico', 85.00, 120), 
('Monitor Ultrawide 34"', 1899.90, 30);

SELECT id FROM Clientes WHERE nome = 'Maria';

INSERT INTO Pedidos (id_cliente, total) VALUES
(2, 0.00);

INSERT INTO Itens_Pedido (id_pedido, id_produto, quantidade) VALUES
(1, 1, 1), 
(1, 2, 2);

SELECT
    nome AS "Nome do Produto",
    preco
FROM Produtos
WHERE preco > 100.00;

SELECT
    C.nome AS "Nome do Cliente",
    P.id AS "ID do Pedido",
    P.data_compra AS "Data da Compra"
FROM Pedidos P
INNER JOIN Clientes C ON P.id_cliente = C.id
WHERE C.nome = 'Maria';

UPDATE Produtos
SET preco = preco * 1.10
WHERE nome = 'Mouse Sem Fio Ergonômico';

UPDATE Produtos
SET estoque = estoque - 2
WHERE nome = 'Mouse Sem Fio Ergonômico';

DELETE FROM Clientes
WHERE nome = 'João';

DELETE FROM Itens_Pedido
WHERE id_pedido = 1 AND id_produto = 1;
-- Active: 1759769973598@@127.0.0.1@3306
CREATE TABLE autores(id_auto INTEGER PRIMARY KEY,
nome_autor TEXT NOT NULL,
nacionalidade TEXT NOT NULL
);

CREATE TABLE livros(id_livro INTEGER PRIMARY KEY,
titulo TEXT NOT NULL,
ano_publicado INT,
id_autor INT,FOREIGN KEY(id_autor) REFERENCES autores(id_auto)
);

INSERT INTO autores (id_auto,nome_autor,nacionalidade) VALUES (0012,'Patrick Rothfuss','Americano'
);

INSERT INTO autores (id_auto,nome_autor,nacionalidade) VALUES (13,'J. R. R. Tolkien','britânico'
);

INSERT into livros (titulo,ano_publicado,id_autor) VALUES ('O nome do vento',2007,12
);

INSERT into livros (titulo,ano_publicado,id_autor) VALUES ('O temor do sabio',2011,12
);

INSERT into livros (titulo,ano_publicado,id_autor) VALUES ('O Hobbit',1937,13
);


SELECT * 
FROM autores;

SELECT * 
FROM livros;

SELECT titulo, ano_publicado 
FROM livros;

SELECT livros.titulo, autores.nome_autor 
FROM livros
JOIN autores ON livros.id_autor = autores.id_auto;

SELECT livros.titulo, autores.nome_autor
FROM livros
JOIN autores ON livros.id_autor = autores.id_auto
WHERE autores.nacionalidade = 'britânico';

SELECT autores.nome_autor, COUNT(livros.id_livro) as total_livros
FROM autores
LEFT JOIN livros ON autores.id_auto = livros.id_autor
GROUP BY autores.id_auto, autores.nome_autor;
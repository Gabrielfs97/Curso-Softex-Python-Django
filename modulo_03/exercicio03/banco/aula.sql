-- Active: 1759755578918@@127.0.0.1@3306
CREATE TABLE usuarios (id_use INTEGER PRIMARY KEY,
primeiro_nome TEXT NOT NULL,
sobrenome TEXT NOT NULL,
email TEXT NOT NULL,
senha TEXT NOT NULL
);

CREATE TABLE postagens (id_post INTEGER PRIMARY KEY,
titulo TEXT NOT NULL,
postagem TEXT,id_autor INT, FOREIGN KEY (id_autor) REFERENCES usuarios(id_use));


INSERT INTO usuarios (id_use, primeiro_nome,sobrenome, email, senha) VALUES(3544,'Jorge','Braga','JorgeB@gmail.com','jorgin1212')


INSERT INTO postagens(titulo,postagem,id_autor) VALUES ('visita a avó', 'fui na minha avó e minha avó estava lá', 324 )


SELECT * FROM usuarios;

SELECT * FROM postagens;

DROP TABLE usuarios;

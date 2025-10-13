import sqlite3
from datetime import datetime
from database import DatabaseConnection


class Blogmodel:

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()
    
    def _create_table(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute(

            """
             CREATE TABLE IF NOT EXISTS blog (id_post INTEGER PRIMARY KEY AUTOINCREMENT,
                 titulo TEXT NOT NULL,
                 postagem TEXT,
                 id_autor INT UNIQUE, 
                 FOREIGN KEY (id_autor) REFERENCES usuarios(id_use),
                 data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                 data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
                 ); 

              """

            )
        
        self.db_conn.close()

    def create_post(self,titulo,postagem):

        self.db_conn.connect()

        try:
            self.db_conn.cursor.execute(
            """
              INSERT INTO blog (titulo, postagem, id_autor)
              VALUE (?,?,?)
            """,
            (titulo,postagem)
            )
            print("Post criado com sucesso ")

        finally:

            self.db_conn.close()

    def find_id_post_by_id(self, id_post):

        """Busca um post pelo ID."""

        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blog WHERE id = ?;", (id_post,))
        user = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return user
    
    def update_post_by_id(self, id_post, senha=None, email=None):
        """Atualiza informações de um post pelo ID."""

        self.db_conn.connect()
        updates = []
        params = []
        if senha:

            updates.append("senha = ?")
            params.append(senha)

        if email:

            updates.append("email = ?")
            params.append(email)

        if not updates:

            print("Nenhum dado para atualizar.")
            self.db_conn.close()
            return

        updates.append("data_atualizacao = ?")
        params.append(datetime.now())
        params.append(id_post)

        query = f"UPDATE blog SET {', '.join(updates)} WHERE id = ?;"

        self.db_conn.cursor.execute(query, params)
        print("Postagem atualizado com sucesso!")
        self.db_conn.close()

    def delete_post_by_id(self, id_post):

        """Deleta um post pelo ID."""
        
        self.db_conn.connect()
        self.db_conn.cursor.execute("DELETE FROM blog WHERE id = ?;", (id_post,))
        print("Postagem deletada com sucesso!")
        self.db_conn.close()

    def get_all_post(self):

        """Retorna todos os posts."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blog;")
        users = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return users
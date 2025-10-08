import sqlite3  

conn = sqlite3.connect('meu_banco.db')
print("banco de dados 'meu_banco.db' criado com sucesso")
conn.close()
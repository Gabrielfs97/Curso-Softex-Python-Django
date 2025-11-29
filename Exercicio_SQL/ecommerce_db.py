import sqlite3  

conn = sqlite3.connect('ecommerce.db')
print("banco de dados 'ecommerce.db' criado com sucesso")
conn.close()
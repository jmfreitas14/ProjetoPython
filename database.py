import sqlite3

conn = sqlite3.connect("ProjetoPY.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);
""")

print("Conectado ao banco de dados!!!")

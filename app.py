from flask import Flask, render_template, request, redirect
import sqlite3

# Criação da aplicação Flask
app = Flask(__name__)

# Função para obter a conexão com o banco de dados SQLite
def get_db_connection():
    try:
        conn = sqlite3.connect('BancoDeDados.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Criando função para criação do banco de dados 
def create_table():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cardapio_pizza( 
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome_Pizza TEXT NOT NULL,
            Descrição TEXT NOT NULL, 
            Preco_P REAL NOT NULL,
            Preco_M REAL NOT NULL,
            Preco_G REAL NOT NULL,
            Preco_GG REAL NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cardapio_sobre( 
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome_sobremessa TEXT NOT NULL,
            Preco REAL NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cardapio_bebidas( 
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome_bebida TEXT NOT NULL,
            preco REAL NOT NULL 
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conta( 
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            email TEXT NOT NULL,
            idade INT NOT NULL,
            telefone TEXT NOT NULL,
            senha TEXT NOT NULL
            )
        ''')

        #inserção de dados do caradapios de pizza
        cursor.execute("SELECT COUNT(*) FROM cardapio_pizza")
        if cursor.fetchone()[0] == 0:
            cursor.executemany('''
                INSERT INTO cardapio_pizza (Id, Nome_Pizza, Descrição, Preco_P, Preco_M, Preco_G,Preco_GG) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', [
                    (3,'Pizza Frango','Molho de Tomate, Queijo Mussarela, Frango', 19.00, 21.00, 28.00, 31.00), 
            ])
        

        #inserção de dados do cardapio sobremessa
        cursor.execute("SELECT COUNT(*) FROM cardapio_sobre")
        if cursor.fetchone()[0] == 0:
            cursor.executemany('''
                INSERT INTO cardapio_sobre (Id, Nome_Sobremessa,Preco) VALUES (?, ?, ?)
            ''', [
                    (1,'Pudim', 8.00),
                    (2,'Torta de Limão', 8.00)
            ])

        # Commit e fechamento da conexão
        conn.commit()
        conn.close()


if __name__ == '__main__':
    create_table()
    app.run(debug=True)

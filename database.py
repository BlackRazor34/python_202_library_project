# Şu anda kitap verileri data/books.json içinde tutuluyor. Bunu artık books.db adlı bir SQLite veritabanına taşıyacağız
# Python'da yerleşik olarak gelen sqlite3 modülünü kullanacağız

import sqlite3

def get_db_connection():
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            isbn TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER
        )
    ''')
    conn.commit()
    conn.close()

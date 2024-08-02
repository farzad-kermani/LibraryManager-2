
import sqlite3

def create_table():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publisher TEXT,
            year INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()


def get_all_books():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM books')
    books = c.fetchall()
    
    conn.close()
    
    return books


def add_book(title, author, publisher, year):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, publisher, year) VALUES (?, ?, ?, ?)", (title, author, publisher, year))
    conn.commit()
    conn.close()


def search_books_by_title(title):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + title + '%',))
    books = c.fetchall()
    conn.close()
    return books




def delete_book(book_id):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
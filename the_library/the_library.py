# the_library

import sqlite3
from tabulate import tabulate

# GK COLLABS: THE LIBRARY - FULL CLINICAL CORE 6
# Human Architect: Karen Nelson-185
# AI Draftsman: Gemini

def connect_db():
    return sqlite3.connect('the_library.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    # Book ID is your Primary Key
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            published INTEGER,
            genre TEXT,
            isbn TEXT,
            publisher TEXT
        )
    ''')
    conn.commit()
    conn.close()

def create_book():
    print("\n--- [1] CREATE: ADD NEW BOOK ---")
    b_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    published = input("Year Published: ")
    genre = input("Genre: ")
    isbn = input("ISBN: ")
    publisher = input("Publisher: ")
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (book_id, title, author, published, genre, isbn, publisher) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (b_id, title, author, published, genre, isbn, publisher))
    conn.commit()
    conn.close()
    print("Book successfully archived in The Library.")

def read_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    conn.close()
    headers = ["ID", "Title", "Author", "Published", "Genre", "ISBN", "Publisher"]
    print("\n--- [2] READ: THE LIBRARY ARCHIVE ---")
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def search_books():
    query = input("\nSearch by Title, Author, or ISBN: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM books 
        WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?
    ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
    rows = cursor.fetchall()
    conn.close()
    headers = ["ID", "Title", "Author", "Published", "Genre", "ISBN", "Publisher"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def summary_report():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT genre, COUNT(*) FROM books GROUP BY genre")
    rows = cursor.fetchall()
    conn.close()
    print("\n--- [6] SUMMARY: COLLECTION BY GENRE ---")
    print(tabulate(rows, headers=["Genre", "Count"], tablefmt="grid"))

create_table()

if __name__ == "__main__":
    while True:
        print("\n=== THE LIBRARY TOOLKIT (CORE 6) ===")
        print("1. Create  2. Read  3. Search  4. Summary  5. Exit")
        choice = input("Select Action: ")
        if choice == '1': create_book()
        elif choice == '2': read_books()
        elif choice == '3': search_books()
        elif choice == '4': summary_report()
        elif choice == '5': break
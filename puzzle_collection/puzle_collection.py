# puzle_collection.py

import sqlite3
from tabulate import tabulate

# GK COLLABS: THE PUZZLE COLLECTION - FULL CLINICAL CORE 6
# Human Architect: Karen Nelson-185
# AI Draftsman: Gemini

def connect_db():
    return sqlite3.connect('puzzle_collection.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS puzzles (
            puzzle_id INTEGER PRIMARY KEY,
            puzzle_name TEXT,
            illustrator TEXT,
            publisher TEXT,
            genre TEXT,
            dimensions TEXT,
            piece_count INTEGER,
            isbn TEXT,
            completed TEXT
        )
    ''')
    conn.commit()
    conn.close()

def create_puzzle():
    print("\n--- [1] CREATE: ADD NEW PUZZLE ---")
    p_id = input("Puzzle ID: ")
    name = input("Puzzle Name: ")
    illustrator = input("Illustrator: ")
    publisher = input("Publisher: ")
    genre = input("Genre: ")
    dims = input("Dimensions (e.g., 50x70cm): ")
    count = input("Piece Count: ")
    isbn = input("ISBN: ")
    comp = input("Completed (Yes/No): ")
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO puzzles (puzzle_id, puzzle_name, illustrator, publisher, genre, dimensions, piece_count, isbn, completed) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (p_id, name, illustrator, publisher, genre, dims, count, isbn, comp))
    conn.commit()
    conn.close()
    print("Puzzle successfully archived.")

def read_puzzles():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM puzzles')
    rows = cursor.fetchall()
    conn.close()
    headers = ["ID", "Name", "Illustrator", "Publisher", "Genre", "Dims", "Pieces", "ISBN", "Done?"]
    print("\n--- [2] READ: THE PUZZLE COLLECTION ---")
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def search_puzzles():
    query = input("\nSearch by Name, Illustrator, or Genre: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM puzzles 
        WHERE puzzle_name LIKE ? OR illustrator LIKE ? OR genre LIKE ?
    ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
    rows = cursor.fetchall()
    conn.close()
    headers = ["ID", "Name", "Illustrator", "Publisher", "Genre", "Dims", "Pieces", "ISBN", "Done?"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def summary_report():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT completed, COUNT(*) FROM puzzles GROUP BY completed")
    rows = cursor.fetchall()
    conn.close()
    print("\n--- [6] SUMMARY: COMPLETION STATUS ---")
    print(tabulate(rows, headers=["Completed", "Count"], tablefmt="grid"))

create_table()

if __name__ == "__main__":
    while True:
        print("\n=== PUZZLE COLLECTION TOOLKIT (CORE 6) ===")
        print("1. Create  2. Read  3. Search  4. Summary  5. Exit")
        choice = input("Select Action: ")
        if choice == '1': create_puzzle()
        elif choice == '2': read_puzzles()
        elif choice == '3': search_puzzles()
        elif choice == '4': summary_report()
        elif choice == '5': break
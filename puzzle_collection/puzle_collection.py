# puzzle_collection.py

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

def update_puzzle():
    read_puzzles()  # Shows the grid so they see the Puzzle IDs
    puzzle_id = input("\nEnter the Puzzle ID you wish to update: ")
    
    print("\nWhat would you like to update?")
    print("[1] Puzzle Name")
    print("[2] Illustrator")
    print("[3] Publisher")
    print("[4] Genre")
    print("[5] Dimensions")
    print("[6] Piece Count")
    print("[7] ISBN")
    print("[8] Completed Status (Yes/No)")
    
    sub_choice = input("Enter choice (1-8): ")
    new_value = input("Enter the new correct detail: ")
    
    column_to_update = ""
    if sub_choice == "1":
        column_to_update = "puzzle_name"
    elif sub_choice == "2":
        column_to_update = "illustrator"
    elif sub_choice == "3":
        column_to_update = "publisher"
    elif sub_choice == "4":
        column_to_update = "genre"
    elif sub_choice == "5":
        column_to_update = "dimensions"
    elif sub_choice == "6":
        column_to_update = "piece_count"
    elif sub_choice == "7":
        column_to_update = "isbn"
    elif sub_choice == "8":
        column_to_update = "completed"
    else:
        print("Invalid choice. Returning to main menu.")
        return

    # Clean SQLite execution for GitHub
    conn = sqlite3.connect('puzzles.db')
    cursor = conn.cursor()
    query = f"UPDATE puzzles SET {column_to_update} = ? WHERE puzzle_id = ?"
    
    cursor.execute(query, (new_value, puzzle_id))
    conn.commit()
    conn.close()
    
    print(f"\nSUCCESS: Puzzle ID {puzzle_id}'s {column_to_update} has been updated to '{new_value}'!")

def delete_puzzle():
    read_puzzles()  # Displays the grid first so they can check the correct IDs
    puzzle_id = input("\nEnter the Puzzle ID you wish to DELETE permanently: ")
    
    # Standard Core Six safety confirmation
    confirm = input(f"Are you absolutely sure you want to delete Puzzle ID {puzzle_id}? (yes/no): ").lower()
    
    if confirm == 'yes':
        conn = sqlite3.connect('puzzles.db')
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM puzzles WHERE puzzle_id = ?", (puzzle_id,))
        
        conn.commit()
        conn.close()
        print(f"\nSUCCESS: Puzzle ID {puzzle_id} has been permanently deleted from the collection.")
    else:
        print("\nDeletion cancelled. Returning to main menu.")

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
        print("1. Create  2. Read  3. Update  4. Delete  5. Search  6. Summary  7. Exit")
        choice = input("Select Action: ")
        if choice == '1': create_puzzle()
        elif choice == '2': read_puzzles()
        elif choice == '3': update_puzzle()
        elif choice == '4': delete_puzzle()
        elif choice == '5': search_puzzles()
        elif choice == '6': summary_report()
        elif choice == '7': break

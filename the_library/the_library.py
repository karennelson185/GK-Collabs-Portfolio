# the_library

import sqlite3
from tabulate import tabulate

# GK COLLABS: THE LIBRARY - CORE SIX
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
    
def update_book():
    read_books()  # 1. Present the table so they see the IDs
    book_id = input("\nEnter the Book ID you wish to update: ")
    
    # 2. Offer the user the choice of what to change
    print("\nWhat would you like to update?")
    print("[1] Title")
    print("[2] Author")
    print("[3] Publishing Year")
    print("[4] Genre")
    print("[5] ISBN")
    print("[6] Publisher")
    
    sub_choice = input("Enter choice (1-6): ")
    new_value = input("Enter the new correct detail: ")
    
    # 3. Figure out which column to target based on their choice
    column_to_update = ""
    if sub_choice == "1":
        column_to_update = "title"
    elif sub_choice == "2":
        column_to_update = "author"
    elif sub_choice == "3":
        column_to_update = "published"  # Matches your integer/year column
    elif sub_choice == "4":
        column_to_update = "genre"
    elif sub_choice == "5":
        column_to_update = "isbn"
    elif sub_choice == "6":
        column_to_update = "publisher"
    else:
        print("Invalid choice. Returning to main menu.")
        return

    # 4. Run the dynamic SQL injection safely using Python f-strings for the column name
    conn = connect_db()
    cursor = conn.cursor()
    
    # We use f-string for column name (safe since it's hardcoded above) and %s for user value
    query = f"UPDATE books SET {column_to_update} = ? WHERE book_id = ?"
    
    cursor.execute(query, (new_value, book_id))
    conn.commit()
    conn.close()
    
    print(f"\nSUCCESS: Book ID {book_id}'s {column_to_update} has been updated to '{new_value}'!")
    
def delete_book():
    read_books()  # Displays the grid first so they can see the correct IDs
    book_id = input("\nEnter the Book ID you wish to DELETE permanently: ")
    
    # Safety check—crucial for a professional user experience!
    confirm = input(f"Are you absolutely sure you want to delete Book ID {book_id}? (yes/no): ").lower()
    
    if confirm == 'yes':
        conn = connect_db()
        cursor = conn.cursor()
        
        # Executes the clean delete targeting the primary key
        cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
        
        conn.commit()
        conn.close()
        print(f"\nSUCCESS: Book ID {book_id} has been permanently deleted from the database.")
    else:
        print("\nDeletion cancelled. Returning to main menu.")

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
        print("1. Create  2. Read  3. Update  4. Delete  5. Search  6. Summary  7. Exit")
        choice = input("Select Action: ")
        if choice == '1': create_book()
        elif choice == '2': read_books()
        elif choice == '3': update_book()
        elif choice == '4': delete_book()
        elif choice == '5': search_books()
        elif choice == '6': summary_report()
        elif choice == '7': break
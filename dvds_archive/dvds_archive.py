dvds_archive.py

import sqlite3
from tabulate import tabulate

# GK COLLABS: DVD ARCHIVE - FULL CLINICAL CORE 6
# Human Architect: Karen Nelson-185
# AI Draftsman: Gemini

def connect_db():
    return sqlite3.connect('dvd_archive.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    # Adding Film ID as a specific column alongside the Title and Actors
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dvds (
            film_id INTEGER PRIMARY KEY,
            title TEXT,
            director TEXT,
            lead_actors TEXT,
            lead_actresses TEXT,
            certification TEXT,
            runtime TEXT,
            release_year INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def create_dvd():
    print("\n--- [1] CREATE: ADD NEW FILM ---")
    f_id = input("Film ID: ")
    title = input("Film Title: ")
    director = input("Director: ")
    actors = input("Lead Actors: ")
    actresses = input("Lead Actresses: ")
    cert = input("Certification: ")
    runtime = input("Runtime: ")
    year = input("Release Year: ")
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO dvds (film_id, title, director, lead_actors, lead_actresses, certification, runtime, release_year) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (f_id, title, director, actors, actresses, cert, runtime, year))
    conn.commit()
    conn.close()
    print("Film successfully archived.")

def read_dvds():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dvds')
    rows = cursor.fetchall()
    conn.close()
    headers = ["Film ID", "Title", "Director", "Actors", "Actresses", "Cert", "Runtime", "Year"]
    print("\n--- [2] READ: FILM ARCHIVE ---")
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    
def update_dvd():
    read_dvds()  # Present the grid so they can see the film_ids
    film_id = input("\nEnter the Film ID you wish to update: ")
    
    print("\nWhat would you like to update?")
    print("[1] Title")
    print("[2] Director")
    print("[3] Lead Actor")
    print("[4] Lead Actress")
    print("[5] Release Year")
    print("[6] Genre")
    print("[7] Duration (Mins)")
    print("[8] Rating")
    print("[9] Format (e.g., DVD/Blu-ray)")
    
    sub_choice = input("Enter choice (1-9): ")
    new_value = input("Enter the new correct detail: ")
    
    # Map the number straight to your PGAdmin column headers
    column_to_update = ""
    if sub_choice == "1":
        column_to_update = "title"
    elif sub_choice == "2":
        column_to_update = "director"
    elif sub_choice == "3":
        column_to_update = "lead_actor"
    elif sub_choice == "4":
        column_to_update = "lead_actress"
    elif sub_choice == "5":
        column_to_update = "release_year"
    elif sub_choice == "6":
        column_to_update = "genre"
    elif sub_choice == "7":
        column_to_update = "duration"
    elif sub_choice == "8":
        column_to_update = "rating"
    elif sub_choice == "9":
        column_to_update = "format"
    else:
        print("Invalid choice. Returning to main menu.")
        return

    # Clean, universal SQLite query using the '?' placeholder for GitHub
    conn = sqlite3.connect('dvds.db')
    cursor = conn.cursor()
    query = f"UPDATE dvds SET {column_to_update} = ? WHERE film_id = ?"
    
    cursor.execute(query, (new_value, film_id))
    conn.commit()
    conn.close()
    
    print(f"\nSUCCESS: Film ID {film_id}'s {column_to_update} has been updated to '{new_value}'!")
    
def delete_dvd():
    read_dvds()  # Displays the grid first so they can see the correct Film IDs
    film_id = input("\nEnter the Film ID you wish to DELETE permanently: ")
    
    # Safety confirmation step to prevent accidental deletion
    confirm = input(f"Are you absolutely sure you want to delete Film ID {film_id}? (yes/no): ").lower()
    
    if confirm == 'yes':
        conn = sqlite3.connect('dvds.db')
        cursor = conn.cursor()
        
        # Executes the clean delete targeting the film_id primary key
        cursor.execute("DELETE FROM dvds WHERE film_id = ?", (film_id,))
        
        conn.commit()
        conn.close()
        print(f"\nSUCCESS: Film ID {film_id} has been permanently deleted from the database.")
    else:
        print("\nDeletion cancelled. Returning to main menu.")
    

def search_dvds():
    query = input("\nSearch by Title, Director, or Talent: ")
    conn = connect_db()
    cursor = conn.cursor()
    # Clinical search covering both Actors and Actresses
    cursor.execute('''
        SELECT * FROM dvds 
        WHERE title LIKE ? OR director LIKE ? OR lead_actors LIKE ? OR lead_actresses LIKE ?
    ''', (f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%'))
    rows = cursor.fetchall()
    conn.close()
    headers = ["Film ID", "Title", "Director", "Actors", "Actresses", "Cert", "Runtime", "Year"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def summary_report():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT director, COUNT(*) FROM dvds GROUP BY director")
    rows = cursor.fetchall()
    conn.close()
    print("\n--- [6] SUMMARY: COLLECTION BY DIRECTOR ---")
    print(tabulate(rows, headers=["Director", "Count"], tablefmt="grid"))

# Initialize
create_table()

if __name__ == "__main__":
    while True:
        print("\n=== DVD ARCHIVE TOOLKIT (CORE 6) ===")
        print("1. Create  2. Read  3. Update  4. Delete  5. Search  6. Summary  7. Exit")
        choice = input("Select Action: ")
        if choice == '1': create_dvd()
        elif choice == '2': read_dvds()
        elif choice == '3': update_dvd()
        elif choice == '4': delete_dvd()
        elif choice == '5': search_dvds()
        elif choice == '6': summary_report()
        elif choice == '7': break
        if __name__ == "__main__":
    

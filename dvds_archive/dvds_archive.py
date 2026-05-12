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
        print("1. Create  2. Read  3. Search  4. Summary  5. Exit")
        choice = input("Select Action: ")
        if choice == '1': create_dvd()
        elif choice == '2': read_dvds()
        elif choice == '3': search_dvds()
        elif choice == '4': summary_report()
        elif choice == '5': break

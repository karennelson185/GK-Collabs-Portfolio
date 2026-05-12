# games_compendium.py

import sqlite3
from tabulate import tabulate

# GK COLLABS: GAMES COMPENDIUM - FULL CLINICAL CORE 6
# Human Architect: Karen Nelson-185
# AI Draftsman: Gemini

def connect_db():
    return sqlite3.connect('games_compendium.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            developer TEXT,
            platform TEXT,
            genre TEXT,
            release_year INTEGER,
            nationality TEXT,
            media_type TEXT,
            rating TEXT
        )
    ''')
    conn.commit()
    conn.close()

def create_game():
    print("\n--- [1] CREATE: ADD NEW TITLE ---")
    title = input("Game Title: ")
    developer = input("Developer: ")
    platform = input("Platform (e.g., PS1, PS4, PC): ")
    genre = input("Genre: ")
    year = input("Release Year: ")
    nation = input("Nationality (Developer Origin): ")
    media = input("Media Type (e.g., Disc, Digital, Cartridge): ")
    rating = input("Rating: ")
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO games (title, developer, platform, genre, release_year, nationality, media_type, rating) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (title, developer, platform, genre, year, nation, media, rating))
    conn.commit()
    conn.close()
    print("Game successfully archived in the Compendium.")

def read_games():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM games')
    rows = cursor.fetchall()
    conn.close()
    headers = ["ID", "Title", "Developer", "Platform", "Genre", "Year", "Origin", "Media", "Rating"]
    print("\n--- [2] READ: GAMES ARCHIVE ---")
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def search_games():
    query = input("\nSearch by Title, Developer, or Platform: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM games 
        WHERE title LIKE ? OR developer LIKE ? OR platform LIKE ?
    ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
    rows = cursor.fetchall()
    conn.close()
    headers = ["ID", "Title", "Developer", "Platform", "Genre", "Year", "Origin", "Media", "Rating"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def summary_report():
    conn = connect_db()
    cursor = conn.cursor()
    # Clinical summary of the collection by Platform (PS1, PS2, etc.)
    cursor.execute("SELECT platform, COUNT(*) FROM games GROUP BY platform")
    rows = cursor.fetchall()
    conn.close()
    print("\n--- [6] SUMMARY: COLLECTION BY PLATFORM ---")
    print(tabulate(rows, headers=["Platform", "Count"], tablefmt="grid"))

# Initialize
create_table()

if __name__ == "__main__":
    while True:
        print("\n=== GAMES COMPENDIUM TOOLKIT (CORE 6) ===")
        print("1. Create  2. Read  3. Search  4. Summary  5. Exit")
        choice = input("Select Action: ")
        if choice == '1': create_game()
        elif choice == '2': read_games()
        elif choice == '3': search_games()
        elif choice == '4': summary_report()
        elif choice == '5': break
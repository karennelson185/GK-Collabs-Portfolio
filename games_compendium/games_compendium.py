# games_compendium.py

import sqlite3
from tabulate import tabulate

# GK COLLABS: GAMES COMPENDIUM - CORE SIX
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

def update_game():
    read_games()  # Shows the grid so they see the IDs
    game_id = input("\nEnter the Game ID you wish to update: ")
    
    print("\nWhat would you like to update?")
    print("[1] Game Title")
    print("[2] Developer")
    print("[3] Platform")
    print("[4] Genre")
    print("[5] Release Year")
    print("[6] Nationality")
    print("[7] Media Type (e.g., Disc, Cartridge, Digital)")
    print("[8] Rating")
    
    sub_choice = input("Enter choice (1-8): ")
    new_value = input("Enter the new correct detail: ")
    
    column_to_update = ""
    if sub_choice == "1":
        column_to_update = "game_title"
    elif sub_choice == "2":
        column_to_update = "developer"
    elif sub_choice == "3":
        column_to_update = "platform"
    elif sub_choice == "4":
        column_to_update = "genre"
    elif sub_choice == "5":
        column_to_update = "release_year"
    elif sub_choice == "6":
        column_to_update = "nationality"
    elif sub_choice == "7":
        column_to_update = "media_type"
    elif sub_choice == "8":
        column_to_update = "rating"
    else:
        print("Invalid choice. Returning to main menu.")
        return

    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()
    # Using your table's specific id column name here
    query = f"UPDATE games SET {column_to_update} = ? WHERE game_id = ?"
    
    cursor.execute(query, (new_value, game_id))
    conn.commit()
    conn.close()
    
    print(f"\nSUCCESS: Game ID {game_id}'s {column_to_update} has been updated to '{new_value}'!")

def delete_game():
    read_games()  # Displays the grid first so they can check the correct IDs
    game_id = input("\nEnter the Game ID you wish to DELETE permanently: ")
    
    # Standard Core Six safety confirmation
    confirm = input(f"Are you absolutely sure you want to delete Game ID {game_id}? (yes/no): ").lower()
    
    if confirm == 'yes':
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        
        # Executes the clean delete targeting your specific ID column name
        cursor.execute("DELETE FROM games WHERE game_id = ?", (game_id,))
        
        conn.commit()
        conn.close()
        print(f"\nSUCCESS: Game ID {game_id} has been permanently deleted from the collection.")
    else:
        print("\nDeletion cancelled. Returning to main menu.")

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
        print("1. Create  2. Read  3. Search  4. Summary  5. Update  6. Delete  7. Exit")
        choice = input("Select Action: ")
        if choice == '1': create_game()
        elif choice == '2': read_games()
        elif choice == '3': update_game()
        elif choice == '4': delete_game()
        elif choice == '5': search_games()
        elif choice == '6': summary_report()
        elif choice == '7': break

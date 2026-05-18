# music_compilation.py


# ================================================== 
#==** GK COLLABS: THE MUSIC COMPILATION DATABASE **==
# Human Designer: Karen Nelson
# AI Draftsman: Gemini
# May 2026
# ===================================================

# **    THIS PYTHON SCRIPT CAN BE USED IN EITHER SQLITE3 AND PGADMIN 4.  JUST SWAP THE ? FOR %s PLACE HOLDERS ##

# import re
# import psycopg2

import sqlite3
from tabulate import tabulate

def connect_db():
    return sqlite3.connect('music_compilation.db')

 # def connect_db()
   # return psycopg2.connect(database=”your_db”, user=”your_username”, password=”your_password”, host=”your_host”, port=”your_port”)

def create_tables():
    try:
        # Connecting straight to your clean 'music' container
       conn  =  connect_db()
       cursor = conn.cursor()


       # 1. THE PARENT TABLE: albums 
       cursor.execute("""
           CREATE TABLE IF NOT EXISTS albums (
               album_id SERIAL PRIMARY KEY,
               album_title VARCHAR(100) NOT NULL,
               artist VARCHAR(100) NOT NULL,
               year VARCHAR(4),
               label VARCHAR(100),
               genre VARCHAR(50),
               producer VARCHAR(100),
               format VARCHAR(20) NOT NULL
           );
       """)
        # 2. THE CHILD TABLE: tracks 
        # Using ON DELETE CASCADE so deleting an album wipes its tracks automatically!
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tracks (
                track_id SERIAL PRIMARY KEY,
                album_id INT REFERENCES albums(album_id) ON DELETE CASCADE,
                track_number INT NOT NULL,
                title VARCHAR(100) NOT NULL,
                songwriter VARCHAR(100),
                duration VARCHAR(7) NOT NULL
            );
        """)
        # Commit the blueprint to the system, then sweep up
        conn.commit()
        cursor.close()
        conn.close()
      
    except Exception as e:
        print(f"[X] An error occurred while laying foundations: {e}")


# This makes sure the tables build immediately when you test run the script
if __name__ == "__main__":
    create_tables()


def add_album_and_tracks():
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    
    print("\n=== STEP 1: ENTER ALBUM DETAILS (PARENT) ===")
    title = input("Album Title: ").strip()
    artist = input("Artist/Band: ").strip()
    year = input("Release Year: ").strip()
    label = input("Record Label: ").strip()
    genre = input("Genre: ").strip()
    producer = input("Producer: ").strip()
    format = input("Format (CD/Vinyl/Download): ").strip()
    
    # 1. Insert into Parent table and dynamically grab the new SERIAL primary key
    try:
        insert_album_sql = """
            INSERT INTO albums (album_title, artist, year, label, genre, producer, format)
            VALUES (?, ?, ?, ?, ?, ?, ?) RETURNING album_id;
        """
        cursor.execute(insert_album_sql, (title, artist, year, label, genre, producer, format))
        
        # This is where Python catches the newly minted ID number!
        current_album_id = cursor.fetchone()[0]
        print(f"[✓] Album successfully saved! Assigned ID: {current_album_id}")
        
        # 2. STEP 2: The Tracks Loop (Child)
        print("\n=== STEP 2: ENTER TRACK DETAILS (CHILD) ===")
        track_counter = 1
        
        while True:
            print(f"\n--- Track Position #{track_counter} ---")
            track_title = input("Track Title (or type 'done' to finish this album): ").strip()
            
            # If you type 'done', the loop breaks and commits everything
            if track_title.lower() == 'done':
                print(f"[!] Stopping track entry. Total tracks added: {track_counter - 1}")
                break
                
            songwriter = input("Songwriter name: ").strip()
            duration = input("Duration (e.g., 03m45s): ").strip()
            
            # Insert the song, bridging it to the parent using current_album_id
            insert_track_sql = """
                INSERT INTO tracks (album_id, track_number, title, songwriter, duration)
                VALUES (?, ?, ?, ?, ?);
            """
            cursor.execute(insert_track_sql, (current_album_id, track_counter, track_title, songwriter, duration))
            print(f"[✓] Added: Track {track_counter} - '{track_title}'")
            
            # Automatically advance the track counter for the next record
            track_counter += 1
            
        # Commit all modifications securely to the system
        conn.commit()
        print(f"\n[✓] Transaction locked! '{title}' and all tracks are fully live in the database.")
        
    except Exception as e:
        conn.rollback() # If anything crashes, roll back so the database doesn't get corrupted
        print(f"[X] Transaction failed. Wiping changes and rolling back: {e}")
    finally:
        cursor.close()
        conn.close()


def read_and_summarize_catalog():
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    
    try:
        # 1. Fetch and print the detailed grid of albums
        cursor.execute("SELECT album_id, album_title, artist, year, genre, format FROM albums ORDER BY artist;")
        albums = cursor.fetchall()
        
        print("\n=============================== THE MUSIC MANOR CATALOG ===============================")
        headers = ["ID", "Album Title", "Artist/Band", "Year", "Genre", "Format"]
        print(tabulate(albums, headers=headers, tablefmt="grid"))
        
        # 2. Run the dynamic aggregation query for the summary block at the bottom
        cursor.execute("SELECT format, COUNT(*) FROM albums GROUP BY format ORDER BY format;")
        summary_rows = cursor.fetchall()
        
        print("\n------------------------------ THE MUSIC COMPILATION: SUMMARY ------------------------------")
        total_albums = 0
        for row in summary_rows:
            # Prints like: "Total Vinyls: 12"
            print(f" • Total {row[0]}s: {row[1]}")
            total_albums += row[1]
        print(f" • TOTAL ASSETS ACROSS THE COMPILATION: {total_albums}")
        print("=” * 46)
        
    except Exception as e:
        print(f"[X] Could not read catalog summary: {e}")
    finally:
        cursor.close()
        conn.close()


def view_album_tracks():
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    
    print("\n=== VIEW ALBUM TRACKLIST ===")
    target_id = input("Enter the Album ID to pull up its tracklist: ").strip()
    
    try:
        # Fetch the album name first to show as a header
        cursor.execute("SELECT album_title, artist FROM albums WHERE album_id = ?;", (target_id,))
        album_info = cursor.fetchone()
        
        if not album_info:
            print("[X] No album found with that ID number.  Sorry!")
            return
            
        print(f"\nTracklist for: '{album_info[0]}' by {album_info[1]}")
        
        # Pull the specific tracks associated with this parent ID
        query = """
            SELECT track_number, title, songwriter, duration 
            FROM tracks 
            WHERE album_id = ? 
            ORDER BY track_number;
        """
        cursor.execute(query, (target_id,))
        tracks = cursor.fetchall()
        
        headers = ["#", "Track Title", "Songwriter", "Duration"]
        print(tabulate(tracks, headers=headers, tablefmt="fancy_grid"))
        print("\n")
        
    except Exception as e:
        print(f"[X] Error fetching tracklist: {e}")
    finally:
        cursor.close()
        conn.close()


def regex_search_system():
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    
    print("\n=== ADVANCED REGEX DATA RETRIEVAL ===")
    search_term = input("Search for a song or songwriter (Min 3 characters): ").strip()
    
    # Strictly enforce the 3-character rule
    if len(search_term) < 3:
        print("[X] Search aborted: Security policy requires at least 3 characters to search.")
        return
        
    try:
        # Using ~* for case-insensitive Regular Expression matching in PostgreSQL
        query = """
            SELECT t.title, t.songwriter, t.duration, a.album_title, a.artist 
            FROM tracks t
            JOIN albums a ON t.album_id = a.album_id
            WHERE t.title ~* ? OR t.songwriter ~* ?;
        """
        cursor.execute(query, (search_term, search_term))
        results = cursor.fetchall()
        
        if results:
            print(f"\n[✓] Matching records found for pattern '{search_term}':")
            headers = ["Song Title", "Songwriter", "Duration", "From Album", "Artist"]
            print(tabulate(results, headers=headers, tablefmt="grid"))
            print("\n")
        else:
            print(f"[-] No tracks or songwriters matched the pattern: '{search_term}'\n")
            
    except Exception as e:
        print(f"[X] RegEx search execution failed: {e}")
    finally:
        cursor.close()
        conn.close()


def delete_album():
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    
    print("\n=== DELETE ALBUM ===")
    target_id = input("Enter the Album ID you wish to permanently remove: ").strip()
    
    # Verification check to make sure you don't delete by accident
    confirm = input(f"Are you absolutely sure you want to delete Album ID {target_id}? (type 'YES' to confirm): ")
    if confirm != "YES":
        print("[!] Deletion canceled. Data intact.")
        return
        
    try:
        # ON DELETE CASCADE handles the track deletion completely in the background!
        cursor.execute("DELETE FROM albums WHERE album_id = ?;", (target_id,))
        conn.commit()
        print(f"[✓] Album ID {target_id} and all its associated track links successfully purged.\n")
        
    except Exception as e:
        conn.rollback()
        print(f"[X] Delete execution failed: {e}")
    finally:
        cursor.close()
        conn.close()


def main_menu():
    # 1. Clear the screen (optional but looks amazing)
    print("\033[H\033[J") 
    
    # 2. YOUR ORIGINAL DRAFTSMAN HEADER PRINTED TO TERMINAL
    print("==========================================================================")
    print(" PROJECT: THE MUSIC COMPILATION DATABASE v1.0                             ")
    print(" REPOSITORY: GK COLLABS PORTFOLIO                                         ")
    print(" AUTHOR / HUMAN ARCHITECT: KAREN NELSON                                   ")
    print(" TECHNICAL DRAFTSMAN: GEMINI                                              ")
    print("==========================================================================")
    print("\n") # Drops down a line for breathing room
    
    # 3. Spin up your system tables background engine
    create_tables()
    
    # 4. Continuous User Interface Loop
    while True:
        print("==============================================")
        print("                 DATABASE MENU                ")
        print("==============================================")
        print”\n”)
        print(“ WELCOME TO THE MUSIC COMPILATION DATABASE”)
        print(" [1] Add New Album and Tracks")
        print(" [2] View Catalogue & Compilation Summary")
        print(" [3] View Album Tracklist")
        print(" [4] Advanced RegEx Search (Songs/Songwriters)")
        print(" [5] Delete Album Entry")
        print(" [6] Exit Database Menu")
        print(“\n”)
        print("=" * 46)
        
        choice = input("Select a system operation (1-6): ").strip()
        
        if choice == '1':
            add_album_and_tracks()
        elif choice == '2':
             read_and_summarize_catalog()
        elif choice == '3':
            view_album_tracks()
        elif choice == '4':
            regex_search_system()
        elif choice == '5':
            delete_or_update_entry()
        elif choice == '6':
            print("\nShutting down The Database. Goodbye!")
            break
        else:
            print("\n[X] Invalid selection. Please choose a number between 1 and 6.\n")


if __name__ == “__main__”:
    main_menu()

# Games Bulk Delete Scripts

import psycopg2

conn = psycopg2.connect(
     user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"
)
cursor = conn.cursor()

# --- The Bulk Eraser ---
print("--- WARNING: Bulk Deletion Mode ---")
genre_to_wipe = input("Enter the GENRE you want to completely remove: ")

confirm = input(f"Are you 100% sure you want to delete EVERY {genre_to_wipe} game? (yes/no): ")

if confirm.lower() == 'yes':
    query = "DELETE FROM games WHERE genre = %s;"
    cursor.execute(query, (genre_to_wipe,))
    conn.commit()
    print(f"The Elephant has forgotten every single {genre_to_wipe} game.")
else:
    print("Action cancelled. Your games are safe.")


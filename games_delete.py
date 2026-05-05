# Games Delete Script

import psycopg2

conn = psycopg2.connect(
     user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"
)
cursor = conn.cursor()

# --- The Eraser: games_delete.py ---
print("--- Delete a Game Record ---")

delete_id = input("Enter the ID of the game you want the Elephant to forget: ")

# The 'Confirm' step (The Safety Catch)
confirm = input(f"Are you SURE you want ID {delete_id} to be forgotten? (yes/no): ")

if confirm.lower() == 'yes':
    query = "DELETE FROM games WHERE game_id = %s;"
    cursor.execute(query, (delete_id,))
    conn.commit()
    print(f"\nRecord {delete_id} is now forgotten by the Elephant.")
else:
    print("\nThe Elephant keeps its memory! No records were removed.")
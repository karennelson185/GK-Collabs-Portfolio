# Games Update Script

import psycopg2

conn = psycopg2.connect(
     user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"
)

print("--- Update Game Details ---")
game_id = input("Enter the ID of the game to update: ")
new_genre = input("Enter new Genre: ")

query = "UPDATE games SET genre = %s WHERE game_id = %s;"
cursor.execute(query, (new_genre, game_id))

conn.commit()
print("Record updated successfully!")
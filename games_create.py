# Games Create Script

import psycopg2

# Connection to your new database
conn = psycopg2.connect(
    
     user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"

)
cursor = conn.cursor()

print("--- Add a New Game to the Library ---")
title = input("Game Title: ")
year = input("Release Year: ")
genre = input("Genre: ")
rating = input("PEGI Rating: ")
plat_id = input("Platform ID (from your Cheat Sheet): ")
dev_id = input("Developer ID (from your Cheat Sheet): ")

# Notice we have 6 placeholders (%s) now
query = "INSERT INTO games (title, release_year, genre, rating, platform_id, developer_id) VALUES (%s, %s, %s, %s, %s, %s);"

cursor.execute(query, (title, year, genre, rating, plat_id, dev_id))

conn.commit()
print(f"Successfully added {title} to the database!")

cursor.close()
conn.close()
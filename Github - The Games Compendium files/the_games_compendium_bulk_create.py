# Games Bulk Create Script

import psycopg2

# The Data 
# You can add as many games as you like in this list!
# (Title, Year, Genre, Rating, Plat_ID, Dev_ID)

games_to_add = [
    ('', , '', '', , ), 
    ('', , '', '', , ),
    ('', , '', '', , )
]

# The Connection

conn = psycopg2.connect(
     user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"
)
cursor = conn.cursor()

# The Execution and Cleanup

query = "INSERT INTO games (title, release_year, genre, rating, platform_id, developer_id) VALUES (%s, %s, %s, %s, %s, %s);"

cursor.executemany(query, games_to_add)
conn.commit()

print(f"Bulk upload complete! {cursor.rowcount} games added.")

cursor.close()
conn.close()
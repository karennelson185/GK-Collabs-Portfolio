# Games Search Script

import psycopg2

conn = psycopg2.connect(
     user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"
)

print("--- Search for a Game ---")
search_term = input("Enter game title to search for: ")

query = """
SELECT games.title, platforms.platform_name, developers.developer_name 
FROM games
JOIN platforms ON games.platform_id = platforms.platform_id
JOIN developers ON games.developer_id = developers.developer_id
WHERE games.title ILIKE %s;
"""

cursor.execute(query, (f"%{search_term}%",))
results = cursor.fetchall()

if results:
    for row in results:
        print(f"Found: {row[0]} on {row[1]} (Dev: {row[2]})")
else:
    print("No games found with that name.")
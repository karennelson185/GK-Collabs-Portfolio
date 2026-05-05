# DVD Read Script

import psycopg2

conn = psycopg2.connect( 
        user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database")
cur = conn.cursor()

cur.execute("SELECT film_id, title, director, release_year FROM dvds ORDER BY title ASC;")
rows = cur.fetchall()

print("\n--- DVD COLLECTION LIST ---")
for row in rows:
    print(f"ID: {row[0]} | {row[1]} ({row[3]}) | Dir: {row[2]}")

cur.close()
conn.close()
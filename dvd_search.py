# DVD Search Script

import psycopg2

conn = psycopg2.connect(
     user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"
)
cur = conn.cursor()

# Keyword set to default.  Insert search term in ''.  Delete when search is complete.
keyword = 'default'
cur.execute("SELECT title, director FROM dvds WHERE title ILIKE %s", (f'%{keyword}%',))
results = cur.fetchall()

print(f"\nSearch results for '{keyword}':")
for r in results:
    print(f"- {r[0]} (Directed by {r[1]})")

cur.close()
conn.close()
# DVD Summary Script

import psycopg2

conn = psycopg2.connect(
     user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"
    )
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM dvds;")
total = cur.fetchone()[0]

print(f"\nTotal DVDs currently in database: {total}")

cur.close()
conn.close()
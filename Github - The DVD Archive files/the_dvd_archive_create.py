# DVD Create Script

import psycopg2

conn = psycopg2.connect(database="your_db_name", user="your_username", password="your_password", host="your_host", port="your_port")
cur = conn.cursor()

# Add as many films as you like to this list
new_film = ('', '', '', '', '', '', '', , )

query = "INSERT INTO dvds (title, director, lead_actor, lead_actress, genre, media_source, certification, runtime, release_year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
cur.execute(query, new_film)

conn.commit()
print(f"Successfully added {title} film to the database.")

cur.close()
conn.close()


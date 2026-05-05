# DVD Delete Script

import psycopg2

conn = psycopg2.connect( 
        user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database")
cur = conn.cursor()

# Change this to the ID you want to remove
id_to_remove = 114

cur.execute("DELETE FROM dvds WHERE film_id = %s", (id_to_remove,))

conn.commit()
print(f"Deleted film with ID: {id_to_remove}")

cur.close()
conn.close()

# DVD Update Script

import psycopg2

conn = psycopg2.connect(
     user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"
)
cur = conn.cursor()

# Change these two variables to target a specific film
target_id = 114
new_runtime = 148

cur.execute("UPDATE dvds SET runtime = %s WHERE film_id = %s", (new_runtime, target_id))

conn.commit()
print(f"Update Complete: ID {target_id} now has runtime {new_runtime}.")

cur.close()
conn.close()
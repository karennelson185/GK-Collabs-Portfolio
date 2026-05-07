# DVD Read Script ~ May 2026


import psycopg2
from tabulate import tabulate

# 1. Connect to the Compendium
# Ensure your password is correct!
conn = psycopg2.connect(
    database="compendium", 
    user="postgres", 
    password="your_password", 
    host="127.0.0.1", 
    port="5432"
)
cur = conn.cursor()

# 2. The Direct Selection Query
# We use film_id, title, release_year, director, genre, and media_source
query = """
SELECT film_id, title, release_year, director, genre, media_source
FROM dvds
ORDER BY title ASC;
"""

# 3. Execute and Fetch
cur.execute(query)
records = cur.fetchall()

# 4. Professional Headers
headers = ["ID", "Title", "Year", "Director", "Genre", "Source"]

print("\n--- THE GK COLLABS DVD ARCHIVE ---")

# 5. The Professional Grid
# Using maxcolwidths to keep the table narrow and tidy for printing
print(tabulate(
    records, 
    headers=headers, 
    tablefmt="grid", 
    maxcolwidths=[None, 25, None, 20, 15, None]
))

print(f"\nTotal volumes in archive: {len(records)}")

# 6. Clean up
cur.close()
conn.close()
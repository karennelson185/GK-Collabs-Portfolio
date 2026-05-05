# Games Read Script - May 2026 - Final Draft

import psycopg2
from tabulate import tabulate

# 1. Connect to the Compendium
# As always, replace 'your_password' with your actual database password
conn = psycopg2.connect(
   user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"
)
cur = conn.cursor()

# 2. The GK Collabs Hybrid Query
# JOINs for Developer and Platform IDs, Direct pull for Genre Name
query = """
SELECT g.game_id, g.title, g.release_year, dev.developer_id, g.genre, p.platform_id
FROM games g
JOIN developers dev ON g.developer_id = dev.developer_id
JOIN platforms p ON g.platform_id = p.platform_id
ORDER BY g.title ASC;
"""

# 3. Execute and Fetch
cur.execute(query)
records = cur.fetchall()

# 4. Professional Headers (Must match the 6 columns in the SELECT)
headers = ["ID", "Title", "Year", "Developer", "Genre", "Platform"]

print("\n--- THE GK COLLABS GAMES ARCHIVE ---")

# 5. The Professional Grid
# Setting specific widths to ensure it looks perfect on the terminal and paper
print(tabulate(
    records, 
    headers=headers, 
    tablefmt="grid", 
    maxcolwidths=[None, 20, None, 15, None, None]
))

print(f"\nTotal volumes in archive: {len(records)}")

# 6. Clean up the connection
cur.close()
conn.close()
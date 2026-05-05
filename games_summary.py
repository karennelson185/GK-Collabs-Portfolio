# Games Summary Script

import psycopg2

conn = psycopg2.connect(
     user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"
)

print("--- Games Library: Executive Summary ---")

# 1. Total Count
cursor.execute("SELECT COUNT(*) FROM games;")
total = cursor.fetchone()[0]

# 2. Breakdown by Platform
cursor.execute("""
    SELECT p.platform_name, COUNT(g.game_id) 
    FROM platforms p
    LEFT JOIN games g ON p.platform_id = g.platform_id
    GROUP BY p.platform_name
    ORDER BY COUNT(g.game_id) DESC;
""")
platforms = cursor.fetchall()

# 3. Breakdown by Developer
cursor.execute("""
    SELECT d.developer_name, COUNT(g.game_id) 
    FROM developers d
    LEFT JOIN games g ON d.developer_id = g.developer_id
    GROUP BY d.developer_name
    HAVING COUNT(g.game_id) > 0
    ORDER BY COUNT(g.game_id) DESC;
""")
developers = cursor.fetchall()

print(f"\nTotal Games in Collection: {total}")
print("\nGames per Platform:")
for p in platforms:
    print(f"- {p[0]}: {p[1]}")

print("\nTop Developers in your Library:")
for d in developers:
    print(f"- {d[0]}: {d[1]}")

cursor.close()
conn.close()
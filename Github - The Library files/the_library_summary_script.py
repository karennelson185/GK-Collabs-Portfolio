# The Library ~ Summary Script ~ May 2026

import psycopg2
from tabulate import tabulate

def library_summary():
    print("\n--- GK COLLABS: THE 8-SET [SUMMARY] ---")
    try:
        conn = psycopg2.connect(dbname="library", user="your_username", password="your_password", host="localhost")
        cur = conn.cursor()
        
        cur.execute("SELECT genre, COUNT(*) FROM books GROUP BY genre ORDER BY COUNT(*) DESC;")
        summary = cur.fetchall()
        
        print(tabulate(summary, headers=["Genre", "Count"], tablefmt="fancy_grid"))
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    library_summary()
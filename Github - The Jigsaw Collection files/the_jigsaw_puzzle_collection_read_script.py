# Jigsaw Puzzle Collection Read Script ~ May 2026

import psycopg2
from tabulate import tabulate

def read_jigsaws():
    try:
        # Connection to your PGAdmin database
        conn = psycopg2.connect(
            database="jigsaw_db", 
            user="postgres", 
            password="YOUR_PASSWORD",  
            host="127.0.0.1", 
            port="5432"
        )
        cur = conn.cursor()

        # The query you mentioned: Ordered by ID
        query = "SELECT * FROM jigsaws ORDER BY title ASC;"
        cur.execute(query)
        
        rows = cur.fetchall()

        # Printing the summary in that clean grid you like
        headers = ["Title", "Illustrator", "Publisher", "Pieces", "Status"]
        print("\n--- GK COLLABS: JIGSAW PUZZLE INVENTORY ---")
        print(tabulate(rows, headers=headers, tablefmt="psql"))

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_jigsaws()
# Jigsaw Puzzle Collection Search Script ~ May 2026

import psycopg2
from tabulate import tabulate

def search_puzzles():
    term = input("Search by Name or Illustrator: ")
    pattern = f"%{term}%"
    try:
        conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="your_host", port="your_port")
            cur = conn.cursor()
        cur.execute("SELECT * FROM puzzles WHERE puzzle_name ILIKE %s OR illustrator ILIKE %s;", (pattern, pattern))
        results = cur.fetchall()
        
        headers = ["ID", "Name", "Artist", "Pieces", "Brand", "Size", "Genre", "Status"]
        print(tabulate(results, headers=headers, tablefmt="grid"))
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_puzzles()
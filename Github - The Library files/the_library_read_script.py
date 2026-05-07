# The Library ~ Read Script ~ May 2026

import psycopg2
from tabulate import tabulate

def read_library():
    try:
        # 1. Connect to the Blue Elephant
        conn = psycopg2.connect(
            dbname="library",
            user="your_username", 
            password="your_password",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # 2. Fetch the books
        query = "SELECT book_id, title, author, published, genre FROM books ORDER BY book_id ASC;"
        cur.execute(query)
        rows = cur.fetchall()

        # 3. Define Headers for the 8-Set Standard
        headers = ["ID", "Title", "Author", "Year", "Genre"]
        
        # 4. Generate the Grid
        table = tabulate(rows, headers=headers, tablefmt="grid")

        # 5. Output to Screen
        print("\n--- GK COLLABS: THE 8-SET LIBRARY SUITE ---")
        print(table)
        print(f"\nTotal Books: {len(rows)}")

        # 6. The "Bridge" Feature: Save to File
        with open("library_report.txt", "w") as f:
            f.write("GK COLLABS LIBRARY REPORT\n")
            f.write("="*30 + "\n")
            f.write(table)
        
        print("\n[System] Report saved to library_report.txt")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_library()
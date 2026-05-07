# The Library ~ Search Script ~ May 2026

import psycopg2
from tabulate import tabulate

def search_library():
    print("\n--- GK COLLABS: THE 8-SET [SEARCH] ---")
    term = input("Search by Title or Author: ")

    try:
        conn = psycopg2.connect(dbname="library", user="your_username", password="your_password", host="localhost")
        cur = conn.cursor()
        query = "SELECT book_id, title, author, genre FROM books WHERE title ILIKE %s OR author ILIKE %s"
        search_data = (f'%{term}%', f'%{term}%')
        
        cur.execute(query, search_data)
        results = cur.fetchall()

        if results:
            table = tabulate(results, headers=["ID", "Title", "Author", "Genre"], tablefmt="grid")
            print(table)
            
            # Save search result to file
            with open("search_results.txt", "w") as f:
                f.write(f"Search Results for: {term}\n")
                f.write(table)
        else:
            print("No books found.")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_library()
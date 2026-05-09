# The DVD Archive Search Script

import psycopg2
from tabulate import tabulate

def search_dvd():
    term = input("Search by Name or Director: ")
    pattern = f"%{term}%"
    try:
        conn = psycopg2.connect(user="your_username", password="your_password", host="your_host", port="your_port", database="your_database")
        cur = conn.cursor()
        cur.execute("SELECT title, director FROM dvds WHERE title ILIKE %s OR director ILIKE %s;", (pattern, pattern))
        results = cur.fetchall()

        headers = ["Name, Director"]
        print(tabulate(results, headers=headers, tablefmt="psql"))

        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}"0

if __name__ == "__main__":
    search_dvd()
     

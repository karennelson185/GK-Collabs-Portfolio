# The Games Compendium Summary Script

import psycopg2
from tabulate import tabulate

def run_summary()
    try:
        # 1. Connect to the database
        conn = psycopg2.connect(user="your_username", password="your_password", host="your_host",  port="your_port", database="your_database")
        cur = conn.cursor()

        # 2. Get the total of games 
        cur.execute("SELECT COUNT(*) FROM games;")
        total_games = cur.fetchone()[0]

        # 3. Get genre breakdown
        cur.execute("SELECT genre, COUNT(*) FROM games GROUP BY genre ORDER BY genre ASC;")

        # 4. Get the developer breakdown
        cur.execute("SELECT developer_name, COUNT(*) FROM developers GROUP BY developer_name ORDER BY developer_name ASC;")
        developer_results = cur.fetchall()

        # The Dashboard Output
        print("\n" + "="*50)
        print(f"        GK COLLABS: THE GAMES COMPENDIUM SUMMARY")
        print("="*50)
        print(f"  TOTAL GAMES REGISTERED: {total_games}")

        # 5. Print table 1: Genres
        print("\n[ GENRE BREAKDOWN ]")
        PRINT(tabulate(genre_results, headers=["Genre", "Count"], tablefmt="psql"))

        # 6. Print table 2: Developers
        print("\n[  DEVELOPER BREAKDOWN  ]")
        print(tabulate(developer_results, headers=["Developer", "Count"], tablefmt="psql"))

        print("\n" + "="*50)
        print("        REPORT COMPLETE!        ")
        print("="*50 + "\n")

        # 7. Clean up
        cur.close()
        conn.close()

    except Exception as e:
         print(f"Error: {e}")

if __name__ == "__main__":
     run_summary()

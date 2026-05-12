# The DVD Archive Summary Script ~ May 2026

import psycopg2
from tabulate import tabulate

def run_summary():
    try:
        # 1. Connect to the Blue Elephant
        conn = psycopg2.connect(
            dbname="dvd_archive", 
            user="your_username", 
            password="your_password", 
            host="localhost", 
            port="5432"
        )
        cur = conn.cursor()

        # 2. Get the Grand Total
        cur.execute("SELECT COUNT(*) FROM dvds;")
        total_dvds = cur.fetchone()[0]

        # 3. Get Genre Breakdown
        cur.execute("SELECT genre, COUNT(*) FROM dvds GROUP BY genre ORDER BY genre ASC;")
        genre_results = cur.fetchall()

        # 4. Get Director Breakdown
        cur.execute("SELECT director, COUNT(*) FROM dvds GROUP BY director ORDER BY director ASC;")
        director_results = cur.fetchall()

        # --- THE DASHBOARD OUTPUT ---
        print("\n" + "="*50)
        print(f"       📀 GK COLLABS: DVD COLLECTION SUMMARY")
        print("="*50)
        print(f" TOTAL DVDS REGISTERED: {total_dvds}")
        print("="*50)

        # Print Table 1: Genres
        print("\n[ GENRE BREAKDOWN ]")
        print(tabulate(genre_results, headers=["Genre", "Count"], tablefmt="grid"))

        # Print Table 2: Directors
        print("\n[ DIRECTOR BREAKDOWN ]")
        print(tabulate(director_results, headers=["Director", "Count"], tablefmt="grid"))

        print("\n" + "="*50)
        print("         REPORT COMPLETE - COYG! 🔴⚪️")
        print("="*50 + "\n")

        # 5. Clean up
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_summary()

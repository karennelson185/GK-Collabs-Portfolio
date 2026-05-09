# The Games Compendium Search Script

import psycopg2
from tabulate import tabulate

def search_game():
    print("\n===**   THE GAMES COMPENDIUM:  SEARCH  **===")
    term = input("\nSearch by Title or Genre: ")
    try:
        conn = psycopg2.connect(
        user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database
        )
        cur = conn.cursor()

        title_query = "SELECT game_id, title, genre FROM games WHERE title ILIKE %s OR genre ILIKE %s ORDER BY game_id ASC"
        search_data =(f%{term}%", f"%{term}%")
        cur.execute(title_query, search_data)

        results = cur.fetchall()

        if results
            print("\n")
            print("Here are your results: ")
            print("\n")
            print(tabulate(results, headers=["ID", "Title", "Genre"], tablefmt="psql"))

        else:
             print("No games found.  Sorry!")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
     search_game()
     


print("--- Search for a Game ---")
search_term = input("Enter game title to search for: ")

query = """
SELECT games.title, platforms.platform_name, developers.developer_name 
FROM games
JOIN platforms ON games.platform_id = platforms.platform_id
JOIN developers ON games.developer_id = developers.developer_id
WHERE games.title ILIKE %s;
"""

cursor.execute(query, (f"%{search_term}%",))
results = cursor.fetchall()

if results:
    for row in results:
        print(f"Found: {row[0]} on {row[1]} (Dev: {row[2]})")
else:
    print("No games found with that name.")

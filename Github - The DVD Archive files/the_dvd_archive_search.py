# The DVD Archive ~ Search Script ~ May 2026

import psycopg2
from tabulate import tabulate

def search_dvds():
    try:
        # 1. Establish Connection
        connection = psycopg2.connect(
            user="your_user",
            password="your_password",
            host="127.0.0.1",
            port="5432",
            database="your_database"
        )
        cursor = connection.cursor()

        # 2. User Input
        print("\n" + "="*30)
        print(" DVD ARCHIVE SEARCH ")
        print("="*30 + "\n")
        
        term = input("Search for a film, director, actor, or actress: ").strip()
        search_query = f"%{term}%"

        # 3. SQL Query (Broad Search)
        query = """
        SELECT title, director, lead_actor, lead_actress, release_year, genre 
        FROM dvds 
        WHERE title ILIKE %s 
        OR director ILIKE %s 
        OR lead_actor ILIKE %s 
        OR lead_actress ILIKE %s;
        """
        
        cursor.execute(query, (search_query, search_query, search_query, search_query))
        results = cursor.fetchall()

        # 4. Smart Display Logic
        if results:
            print(f"\n--- Results found for '{term}' ---")
            
            display_data = []
            headers = []

            for row in results:
                title, director, actor, actress, year, genre = row
                
                # Check if search term matches a person (Actor/Actress/Director)
                if term.lower() in actor.lower() or term.lower() in actress.lower():
                    headers = ["Film Title", "Release Year", "Genre"]
                    display_data.append([title, year, genre])
                
                elif term.lower() in director.lower():
                    headers = ["Film Title", "Lead Actor", "Release Year"]
                    display_data.append([title, actor, year])
                
                # Default: If searching for a specific film title
                else:
                    headers = ["Film Title", "Director", "Lead Talent", "Year"]
                    # Combine actors for a cleaner look in the default view
                    talent = f"{actor} / {actress}"
                    display_data.append([title, director, talent, year])

            # 5. Output the Clean Grid
            print("\n")
            print(tabulate(display_data, headers=headers, tablefmt="grid"))
            print(f"\nTotal records found: {len(results)}\n")

        else:
            print(f"\n[!] No records found for '{term}'.")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Search session closed.\n")

if __name__ == "__main__":
    search_dvds()

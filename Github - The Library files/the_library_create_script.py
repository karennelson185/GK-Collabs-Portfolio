# The Library - Create Script - May 2026

import psycopg2

def add_new_book():
    print("\n--- GK COLLABS: THE 8-SET LIBRARY SUITE [ADD BOOK] ---")
    
    # 1. Collect User Input
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    try:
        published = int(input("Enter Year Published (e.g. 1960 or -375): "))
    except ValueError:
        print("Invalid year. Please enter a number.")
        return
        
    genre = input("Enter Genre: ")
    isbn = input("Enter ISBN: ")
    publisher = input("Enter Publisher: ")

    try:
        # 2. Connect to the Blue Elephant
        conn = psycopg2.connect(
            dbname="library",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # 3. Execute Insert
        query = """
        INSERT INTO books (title, author, published, genre, isbn, publisher)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cur.execute(query, (title, author, published, genre, isbn, publisher))
        
        # 4. Commit and Confirm
        conn.commit()
        print(f"\n[Success] '{title}' has been added to the library!")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    add_new_book()
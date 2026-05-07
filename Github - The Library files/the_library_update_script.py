# The Library ~ Update Script ~ May 2026

import psycopg2

def update_book():
    print("\n--- GK COLLABS: THE 8-SET LIBRARY SUITE [EDIT BOOK] ---")
    
    # 1. Target the specific book
    try:
        book_id = int(input("Enter the Book ID you wish to update: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    # 2. Get the new details
    print("Leave blank and press Enter to keep current value (Optional feature for later!)")
    new_title = input("Enter New Title: ")
    new_author = input("Enter New Author: ")
    new_genre = input("Enter New Genre: ")

    try:
        conn = psycopg2.connect(
            dbname="library",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # 3. Execute the Update
        query = """
        UPDATE books 
        SET title = %s, author = %s, genre = %s
        WHERE book_id = %s;
        """
        cur.execute(query, (new_title, new_author, new_genre, book_id))
        
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"\n[Success] Book ID {book_id} has been updated!")
        else:
            print(f"\n[Error] Book ID {book_id} not found.")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_book()
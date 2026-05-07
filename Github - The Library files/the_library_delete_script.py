# The Library ~ Delete Script ~ May 2026

import psycopg2

def delete_book():
    print("\n--- GK COLLABS: THE 8-SET [DELETE] ---")
    book_id = input("Enter the Book ID to remove: ")
    confirm = input(f"Are you sure you want to delete Book {book_id}? (yes/no): ")

    if confirm.lower() == 'yes':
        try:
            conn = psycopg2.connect(dbname="library", user="your_username", password="your_password", host="localhost")
            cur = conn.cursor()
            cur.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
            conn.commit()
            print(f"\n[System] Book {book_id} removed from library.")
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Deletion cancelled.")

if __name__ == "__main__":
    delete_book()
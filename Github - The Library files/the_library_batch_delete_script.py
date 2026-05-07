# The Library ~ Batch Delete Script - May 2026

import psycopg2

def batch_delete_flagship():
    print("\n--- GK COLLABS: THE 8-SET BATCH REMOVER [CLEAN VERSION] ---")
    ids_to_delete = []
    
    try:
        conn = psycopg2.connect(
            dbname="library",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        while True:
            # 1. Focus only on the ID
            val = input("\nEnter Book ID to delete: ")
            
            try:
                book_id = int(val)
                # Add to our temporary removal list
                ids_to_delete.append(book_id)
                print(f"ID {book_id} added to the removal queue.")
            except ValueError:
                print("Invalid entry. Please enter a numerical ID.")
            
            # 2. The Symmetry: Use the same exit strategy as the Create script
            another = input("\nAdd another ID to this removal batch? (Y/N): ")
            if another.upper() != 'Y':
                break

        if not ids_to_delete:
            print("No IDs entered. Standing down.")
            return

        # 3. The Final "Safety Catch"
        print(f"\nYou have selected {len(ids_to_delete)} books for removal.")
        confirm = input("Are you sure you want to permanently delete these? (Y/N): ")

        if confirm.upper() == 'Y':
            # We use 'IN' to handle the whole list at once
            query = "DELETE FROM books WHERE book_id IN %s;"
            cur.execute(query, (tuple(ids_to_delete),))
            
            conn.commit()
            print(f"\n[Success] {cur.rowcount} books have been removed from the shelf.")
        else:
            print("Deletion cancelled. Data is safe.")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error during database handshake: {e}")

if __name__ == "__main__":
    batch_delete_flagship()
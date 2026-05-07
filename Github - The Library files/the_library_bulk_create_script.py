# The Library ~ Bulk Create Script ~ May 2026

import psycopg2
import csv

def bulk_import():
    print("\n--- GK COLLABS: THE 8-SET [BULK IMPORT] ---")
    filename = "books_data.csv" # Ensure this is in the same folder
    
    try:
        conn = psycopg2.connect(dbname="library", user="your_username", password="your_password", host="localhost")
        cur = conn.cursor()

        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip the header row
            for row in reader:
                cur.execute(
                    "INSERT INTO books (title, author, published, genre, isbn, publisher) VALUES (%s, %s, %s, %s, %s, %s)",
                    row
                )
        
        conn.commit()
        print(f"\n[Success] Bulk upload from {filename} completed.")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    bulk_import()
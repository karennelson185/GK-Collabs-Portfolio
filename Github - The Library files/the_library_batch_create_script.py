# The Library Batch Create Script ~ May 2026

import psycopg2

def batch_create_flagship():
    print("\n--- GK COLLABS: THE 8-SET BATCH CREATE [CLEAN VERSION] ---")
    basket = []
    
    while True:
        # Straight into the data—no counting, no distractions
        title = input("\nEnter Title: ")
        author = input("Enter Author: ")
        
        try:
            published = int(input("Enter Year Published: "))
        except ValueError:
            print("Invalid year. Setting to 0.")
            published = 0
            
        genre = input("Enter Genre: ")
        isbn = input("Enter ISBN: ")
        publisher = input("Enter Publisher: ")

        # Store the book in our temporary session list
        basket.append((title, author, published, genre, isbn, publisher))
        
        # The Exit Strategy: This is the only "Control" line the user needs
        another = input("\nAdd another book to this batch? (Y/N): ")
        if another.upper() != 'Y':
            break

    # The Final "Slap-Slap" Handshake
    if basket:
        print(f"\nReviewing {len(basket)} new entries...")
        confirm = input("Save this batch to the Blue Elephant? (Y/N): ")

        if confirm.upper() == 'Y':
            try:
                conn = psycopg2.connect(
                    dbname="library",
                    user="your_username",
                    password="your_password",
                    host="localhost",
                    port="5432"
                )
                cur = conn.cursor()

                query = """
                INSERT INTO books (title, author, published, genre, isbn, publisher)
                VALUES (%s, %s, %s, %s, %s, %s);
                """
                
                cur.executemany(query, basket)
                conn.commit()
                
                print(f"\n[Success] {len(basket)} books added to the database.")
                cur.close()
                conn.close()

            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Batch discarded.")

if __name__ == "__main__":
    batch_create_flagship()
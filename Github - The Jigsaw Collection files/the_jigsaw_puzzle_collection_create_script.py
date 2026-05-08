# Jigsaw Puzzle Collection Create Script

import psycopg2

def create_puzzle():
    print("\n--- 🧩 ADD NEW JIGSAW PUZZLE ---")
    title = input("Puzzle Name: ")
    artist = input("Illustrator: ")
    genre = input("Genre: ")
    dims = input("Dimensions (e.g., 70x50cm): ")
    pieces = int(input("Piece Count: "))
    isbn = input("ISBN: ")
    brand = input("Publisher: ")
    done = input("Completed? (y/n): ").lower() == 'y'

    try:
        conn = psycopg2.connect(database="jigsaw_library", user="postgres", password="learning123", host="192.168.0.3", port="5432")
        cur = conn.cursor()

        query = """
        INSERT INTO jigsaws (puzzle_name, illustrator, genre, dimensions, piece_count, isbn, publisher, completed) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (title, artist, genre, dims, pieces, isbn, brand, done))
        conn.commit()
        print(f"Successfully added: {name}")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_puzzle()
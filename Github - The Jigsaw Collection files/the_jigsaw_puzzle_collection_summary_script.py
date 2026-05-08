# Jigsaw Puzzle Collection Summary Script ~ May 2026

import psycopg2

def get_summary():
    try:
        conn = psycopg2.connect(dbname="jigsaw_db", user="your_user", password="your_password")
        cur = conn.cursor()
        
        cur.execute("SELECT COUNT(*), SUM(piece_count) FROM puzzles;")
        total_p, total_pieces = cur.fetchone()
        
        cur.execute("SELECT COUNT(*) FROM puzzles WHERE completed = True;")
        finished = cur.fetchone()[0]

        print("\n--- 🧩 JIGSAW COLLECTION SUMMARY ---")
        print(f"Total Puzzles:    {total_p}")
        print(f"Total Pieces:     {total_pieces}")
        print(f"Completed:        {finished}")
        print(f"In Progress:      {total_p - finished}")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_summary()
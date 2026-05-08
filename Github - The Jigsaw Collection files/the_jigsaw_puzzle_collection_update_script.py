# Jigsaw Puzzle Update Script ~ May 2026

import psycopg2

def update_status():
    p_name = input("Enter the puzzle title to mark as completed: ")
    try:
        conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="your_host", port="your_port")
        cur = conn.cursor()
        
        cur.execute("UPDATE jigsaws SET completed = True WHERE puzzle_name = %s;", (p_name,))
        conn.commit()
        print(f"Puzzle {p_name} updated to Completed!")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_status()
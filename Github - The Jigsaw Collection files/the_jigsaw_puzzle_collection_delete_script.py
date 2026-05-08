# Jigsaw Puzzle Collection Delete Script ~ May 2026

import psycopg2

def delete_puzzle():
    p_name = input("Enter puzzle name to remove: ")
    confirm = input(f"Confirm deletion of ID {p_name}? (y/n): ")
    if confirm.lower() == 'y':
        try:
            conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="your_host", port="your_port")
            cur = conn.cursor()
            cur.execute("DELETE FROM puzzles WHERE puzzle_name = %s;", (p_name,))
            conn.commit()
            
            print("Record deleted.")
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    delete_puzzle()
# Job Appn Tracker ~ Read Script

import psycopg2
from tabulate import tabulate
from config import config

def read_jobs():
    print("💼 --- GK Collabs: Current Job Application Pipeline --- 💼\n")
    conn = None
    try:
        # Pull the keys from your new database.ini
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        # Pull the data (Sorting by ID so you see them in order)
        cur.execute("SELECT job_id, job_title, company, app_date, progress FROM job_applications ORDER BY job_id ASC")
        rows = cur.fetchall()
        
        if rows:
            headers = ["ID", "Title", "Company", "Date Applied", "Status"]
            # Your signature psql style!
            print(tabulate(rows, headers=headers, tablefmt="psql"))
        else:
            print("📝 Your tracker is currently empty. Time to log some leads!")
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Database Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    read_jobs()
# Project: Job Application Tracker (job_summary.py)
# Developer: G. Karen Nelson
# Series: GK Collabs - Career Automation Tools
# ---------------------------------------------------------

import psycopg2
from tabulate import tabulate
from config import config

def job_summary():
    print("📊 --- GK Collabs: Career Hunt Summary --- 📊\n")
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        # 1. Total Count
        cur.execute("SELECT COUNT(*) FROM job_applications")
        total = cur.fetchone()[0]
        
        # 2. Status Breakdown
        cur.execute("""SELECT progress, COUNT(*) FROM job_applications GROUP BY progress ORDER BY COUNT(*) DESC""")
        breakdown = cur.fetchall()
        
        print(f"Total Applications Sent: {total}\n")
        print("--- Here is your summary ---")
        print(tabulate(breakdown, headers=["Status", "Count"], tablefmt="psql"))
        print("\nThis session is now closed.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    job_summary()
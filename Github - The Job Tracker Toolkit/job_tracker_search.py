# Project: Job Application Tracker (search_jobs.py)
# Developer: G. Karen Nelson
# Series: GK Collabs - Career Automation Tools
# ---------------------------------------------------------

import psycopg2
from tabulate import tabulate
from config import config

def search_jobs():
    print("🔍 --- GK Collabs: Search Applications --- 🔍\n")
    term = input("Search by Company or Job Title: ")
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        query = """SELECT job_id, job_title, company, progress 
                   FROM job_applications 
                   WHERE company ILIKE %s OR job_title ILIKE %s"""
        cur.execute(query, (f"%{term}%", f"%{term}%"))
        results = cur.fetchall()
        
        if results:
            print(f"\n✅ Found {len(results)} match(es) for '{term}':")
            print(tabulate(results, headers=["ID", "Title", "Company", "Status"], tablefmt="psql"))
        else:
            print(f"\n❌ No applications found matching '{term}'.")
            
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    search_jobs()
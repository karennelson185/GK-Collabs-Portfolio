# Project: Job Application Tracker (search_jobs.py)
# Developer: G. Karen Nelson
# Series: GK Collabs - Career Automation Tools
# ---------------------------------------------------------

import psycopg2
from config import config

def add_job():
    print("💼 --- GK Collabs: Add New Job Application --- 💼\n")
    # 1. Gather User Input
    role = input("Enter Job Title: ")
    company = input("Enter Company Name: ")
    date = input("Date Applied: (YYY-MM-DD) ")
    type = input("Application Type (CV/Online Form/Statement): ")
    status = input("Progress (Applied/Pending/Response): ")
    next_step = input("Interview (y/n): ").lower().strip()
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        # 2. SQL Execution (Notice the Serial job_id handles itself!)
        query = """INSERT INTO job_applications (job_title, company, app_date, app_type, progress, interview) 
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING job_id;"""
        
        cur.execute(query, (role, company, date, app_type, status, next_step))
        job_id = cur.fetchone()[0]
        conn.commit()
        
        print(f"\n✅ Success! Your application for {job_title} is logged as Job ID {job_id} for {company}.")
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    add_job()
# Job Appn Tracker ~ Create Script


import psycopg2
from config import config

def add_job():
    print("💼 --- GK Collabs: Log New Application --- 💼\n")
    
    # 1. Gather User Input
    title = input("Enter Job Title: ")
    company = input("Enter Company Name: ")
    app_type = input("Application Type (e.g., Portfolio, Statement, Form): ")
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        # 2. SQL Execution (Notice the Serial job_id handles itself!)
        sql = """INSERT INTO job_applications (job_title, company, app_type) 
                 VALUES (%s, %s, %s) RETURNING job_id;"""
        
        cur.execute(sql, (title, company, app_type))
        job_id = cur.fetchone()[0]
        conn.commit()
        
        print(f"\n✅ Success! Job ID {job_id} logged for {company}.")
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    add_job()
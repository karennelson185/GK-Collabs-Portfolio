# Project: Job Application Tracker (update_job.py)
# Developer: G. Karen Nelson
# Series: GK Collabs - Career Automation Tools
# ---------------------------------------------------------

import psycopg2
from config import config

def update_status():
    print("📈 --- GK Collabs: Update Application Progress --- 📈\n")
    
    # 1. Get User Input
    job_id = input("Enter the Job ID you want to update: ")
    new_status = input("Enter the new status (e.g., Interview, Response Received, Rejected): ")
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        # 2. Update the logic
        sql = "UPDATE job_applications SET progress = %s WHERE job_id = %s"
        cur.execute(sql, (new_status, job_id))
        
        # Check if anything actually changed
        if cur.rowcount > 0:
            conn.commit()
            print(f"\n✅ Success! Job ID {job_id} is now set to '{new_status}'.")
        else:
            print(f"\n❌ Error: Job ID {job_id} not found.")
            
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Database Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    update_status()
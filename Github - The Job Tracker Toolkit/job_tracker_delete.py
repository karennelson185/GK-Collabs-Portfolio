# Project: Job Application Tracker (delete_job.py)
# Developer: G. Karen Nelson
# Series: GK Collabs - Career Automation Tools
# ---------------------------------------------------------

import psycopg2
from config import config

def delete_job():
    print("🗑️ --- GK Collabs: Remove Application --- 🗑️\n")
    job_id = input("Enter the Job ID to delete: ")
    confirm = input(f"Are you sure you want to delete Job ID {job_id}? (y/n): ")
    
    if confirm.lower() == 'y':
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("DELETE FROM job_applications WHERE job_id = %s", (job_id,))
            conn.commit()
            print(f"\n✅ Job ID {job_id} successfully removed.")
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"❌ Error: {error}")
        finally:
            if conn is not None:
                conn.close()
    else:
        print("\nDeletion cancelled.")

if __name__ == "__main__":
    delete_job()
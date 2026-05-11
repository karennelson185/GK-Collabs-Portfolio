# Project: Job Application Tracker (job_bulk_create.py)
# Developer: G. Karen Nelson
# Series: GK Collabs - Career Automation Tools
# ---------------------------------------------------------

import psycopg2

# 1. THE CONNECTION (Stay outside the loop)

conn = psycopg2.connect(database="job_tracker", user="your_user", password="your_password")
cur = conn.cursor()

print("\n")
print("--- Job Application Tracker: Bulk Entry Mode ---")
print("\n")

# 2. THE LOOP
while True: 
    # Gather Data
    role = input("Job Title: ")
    company = input("Company Name: ")
    date = input("Date Applied: (YYY-MM-DD) ")
    type = input("Application Type (CV/Online Form/Statement): ")
    status = input("Status (Applied/Pending/Response): ")
    next_step = input(Interview (y/n): ").lower().strip()

    # The SQL Execution
    query = "INSERT INTO job_applications (job_title, company, app_date, app_type, progress, interview) VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(query, (role, company, date, type, status, next_step))
    conn.commit()
    
    print(f"You have successfully added {role} to the Job Application Tracker!  Well done!")

    # 3. THE EXIT STRATEGY
    again = input("Add another job? (y/n): ").lower()
    if again != 'y':
        break

# 4. CLEAN UP (Outside the loop)
cur.close()
conn.close()
print("This session is now closed.")
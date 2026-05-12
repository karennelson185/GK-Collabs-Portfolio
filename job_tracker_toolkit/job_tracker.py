# job_tracker.py

import sqlite3
from tabulate import tabulate
from datetime import datetime

# GK COLLABS: JOB TRACKER TOOLKIT - FULL CLINICAL CORE 6
# Human Architect: Karen Nelson-185
# AI Draftsman: Gemini

def connect_db():
    return sqlite3.connect('job_tracker.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT,
            company TEXT,
            date_applied TEXT,
            progress TEXT,
            interview TEXT
        )
    ''')
    conn.commit()
    conn.close()

def create_job():
    print("\n--- [1] CREATE: ADD NEW ENTRY ---")
    title = input("Job Title: ")
    company = input("Company: ")
    date = input("Date Applied (YYYY-MM-DD) [Blank for today]: ")
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    progress = input("Progress (Applied/Screening/Rejected): ")
    interview = input("Interview Scheduled? (Yes/No): ")
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO jobs (job_title, company, date_applied, progress, interview) VALUES (?, ?, ?, ?, ?)', 
                   (title, company, date, progress, interview))
    conn.commit()
    conn.close()
    print("Successfully added to the Manor.")

def read_jobs():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM jobs')
    rows = cursor.fetchall()
    conn.close()
    headers = ["ID", "Job Title", "Company", "Date Applied", "Progress", "Interview"]
    print("\n--- [2] READ: FULL ARCHIVE ---")
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def update_job():
    read_jobs()
    job_id = input("\nEnter ID to Update: ")
    new_progress = input("New Progress Status: ")
    new_interview = input("Update Interview (Yes/No): ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE jobs SET progress = ?, interview = ? WHERE id = ?', (new_progress, new_interview, job_id))
    conn.commit()
    conn.close()
    print("Entry Updated.")

def delete_job():
    read_jobs()
    job_id = input("\nEnter ID to DELETE from Manor: ")
    confirm = input(f"Are you sure you want to delete ID {job_id}? (yes/no): ")
    if confirm.lower() == 'yes':
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM jobs WHERE id = ?', (job_id,))
        conn.commit()
        conn.close()
        print("Entry Removed.")

def search_jobs():
    query = input("\nSearch by Company or Job Title: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs WHERE company LIKE ? OR job_title LIKE ?", (f'%{query}%', f'%{query}%'))
    rows = cursor.fetchall()
    conn.close()
    headers = ["ID", "Job Title", "Company", "Date Applied", "Progress", "Interview"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def summary_report():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT progress, COUNT(*) FROM jobs GROUP BY progress")
    rows = cursor.fetchall()
    conn.close()
    print("\n--- [6] SUMMARY: PROGRESS OVERVIEW ---")
    print(tabulate(rows, headers=["Status", "Count"], tablefmt="grid"))

# Initialize
create_table()

if __name__ == "__main__":
    while True:
        print("\n=== JOB TRACKER TOOLKIT (CORE 6) ===")
        print("1. Create  2. Read  3. Update  4. Delete  5. Search  6. Summary  7. Exit")
        choice = input("Select Action: ")
        if choice == '1': create_job()
        elif choice == '2': read_jobs()
        elif choice == '3': update_job()
        elif choice == '4': delete_job()
        elif choice == '5': search_jobs()
        elif choice == '6': summary_report()
        elif choice == '7': break
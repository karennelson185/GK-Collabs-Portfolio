README.md

![Schematic](./job_schema.png)
# 💼 Job Tracker Toolkit
**Developer:** Karen Nelson | **Series:** GK Collabs

## 📌 Overview
This is a professional suite of Python utilities designed to manage and track job applications within a PostgreSQL database. Built in a Linux (Debian) environment, this toolkit automates the CRUD (Create, Read, Update, Delete) cycle for career management.

## 🚀 Features
* **Automated Data Entry:** Quickly log new roles, companies, and application dates.
* **Status Monitoring:** Update application progress from 'Applied' to 'Interview' or 'Hired'.
* **Search Functionality:** Instantly locate specific roles using SQL-based search queries.
* **Modular Configuration:** Uses a secure `config.py` and `.ini` system to manage database credentials separately from logic.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Database:** PostgreSQL
* **Libraries:** Psycopg2 (Database Driver), Tabulate (CLI Formatting)
* **OS:** Linux (Debian/VirtualBox)
* **Architecture:** Modular Python scripting with a secure config engine.

## 📂 Project Structure
- `job_tracker_create.py`: Entry logic for new applications.
- `job_tracker_read.py`: Displays the full pipeline in a formatted table.
- `config.py`: The helper script for database connectivity.
- `.gitignore`: Ensures local credentials (`database.ini`) remain private.
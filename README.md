# GK Collabs: The Media Management Suite 🚀

Welcome to the **GK Collabs Portfolio**. This project is the result of a 7-day intensive development sprint focused on building robust, relational database solutions for personal media collections. 

Developed in collaboration with **Gemini AI**, this suite demonstrates the power of human-logic paired with AI-assisted architecture.

---

## 📽️ Project Overview
This repository contains a collection of Python-based tools and PostgreSQL database schemas designed to archive, catalog, and query physical and digital media.

### 💿 The DVD Archive
A structured historical database for film collections, featuring relational integrity and optimized search queries.

### 🎮 The Games Compendium
A comprehensive tracking system for gaming libraries, allowing for platform-specific filtering and developer-linked data.

### 📚 The Library (Coming Soon)
A centralized system for book management, utilizing ISBN tracking and imagination-processing logic.

---

## 🛠️ Technical Architecture
* **Language:** Python 3.x
* **Database:** PostgreSQL
* **Libraries:** `psycopg2` for database connectivity, `tabulate` for clean terminal output.
* **Security:** Implementation of a `config_template.py` system to ensure database credentials remain private and secure.

---

## 📊 Database Blueprints (ERDs)
I utilized a "Blueprint-First" approach to ensure data normalization (3NF) and relational efficiency. You can view the technical schemas in the screenshots above, covering:
* **Table Relationships** (Primary & Foreign Keys)
* **Data Ingestion Pipelines**
* **Search Logic Flowcharts**

---

## 🚀 How to Use
1. **Clone the repository:** `git clone https://github.com/YourUsername/GK-Collabs-Portfolio.git`
2. **Setup Credentials:**
   - Rename `config_template.py` to `config.py`.
   - Enter your PostgreSQL `host`, `database`, `user`, and `password`.
3. **Initialize Database:**
   Run the table creation scripts provided in the folders.
4. **Bulk Load Media:**
   Populate your lists in the `bulk_create` scripts and execute to fill your vault!

---

**Designed & Developed by GK Collabs** 🛡️  
🤝 *A positive collaboration between Karen Nelson & Gemini AI*

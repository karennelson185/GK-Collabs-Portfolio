# The DVD Archive Bulk Creation Script ~ May 2026

import psycopg2

def bulk_create_dvds():
    connection = None
    try:
        # 1. Establish the Connection (Lesson 2 Logic)
        connection = psycopg2.connect(
            user="your_user",
            password="your_password",
            host="127.0.0.1",
            port="5432",
            database="your_database"
        )
        cursor = connection.cursor()

        print("\n" + "="*30)
        print(" DVD ARCHIVE: BULK ENTRY ")
        print("="*30)

        while True:
            # 2. Collect Data for one DVD
            print("\n--- Enter Film Details ---")
            title = input("Film Title: ")
            director = input("Director: ")
            lead_actor = input("Lead Actor: ")
            lead_actress = input("Lead Actress: ")
            genre = input("Genre: ")
            media_source = input("Media Source (DVD/Blu-ray): ")
            certification = input("Certification: ")
            runtime = input("Runtime (mins): ")
            release_year = input("Release Year: ")

            # 3. SQL Insert logic
            insert_query = """
            INSERT INTO dvds (title, director, lead_actor, lead_actress, genre, media_source, certification, runtime, release_year)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, (title, director, lead_actor, lead_actress, genre, media_source, certification, runtime, release_year))
            
            # Commit after each entry so data is saved immediately
            connection.commit()
            print(f"\n[SUCCESS] '{title}' added to the archive.")

            # 4. The Loop Control
            again = input("\nWould you like to add another film? (y/n): ").lower().strip()
            if again != 'y':
                break

        print("\nBulk entry complete. All records saved.")

    except (Exception, psycopg2.Error) as error:
        print("\n[ERROR] Database error during bulk creation:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Manor gates closed.\n")

if __name__ == "__main__":
    bulk_create_dvds()

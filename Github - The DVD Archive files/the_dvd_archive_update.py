import psycopg2

def update_dvd_record():
    connection = None
    try:
        # 1. Open the Manor Gates (Lesson 2 Logic)
        connection = psycopg2.connect(
            user="your_user",
            password="your_password",
            host="127.0.0.1",
            port="5432",
            database="your_database"
        )
        cursor = connection.cursor()

        # 2. The Dynamic "Belly" (Recycled from Books logic)
        print("\n--- DVD RECORD UPDATE TOOL ---")
        dvd_id = input("Enter the ID of the DVD you wish to update: ")
        
        print("\nWhich field would you like to update?")
        print("1. Title | 2. Director | 3. Year | 4. Genre")
        choice = input("Enter choice (1-4): ")

        # Mapping the choice to the actual SQL column name
        columns = {"1": "title", "2": "director", "3": "release_year", "4": "genre"}
        column_to_update = columns.get(choice)

        if not column_to_update:
            print("Invalid choice. Aborting.")
            return

        new_value = input(f"Enter the new value for {column_to_update}: ")

        # 3. The Execution
        # We use an f-string for the column name (safe here as we controlled the input)
        # and %s for the data values to prevent SQL injection.
        update_query = f"UPDATE dvds SET {column_to_update} = %s WHERE id = %s"
        
        cursor.execute(update_query, (new_value, dvd_id))
        connection.commit() # The "Save" button

        print(f"\n[SUCCESS] Record {dvd_id} updated. {column_to_update} is now: {new_value}")

    except (Exception, psycopg2.Error) as error:
        print("\n[ERROR] Surgery failed:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("\nManor gates closed.")

if __name__ == "__main__":
    update_dvd_record()

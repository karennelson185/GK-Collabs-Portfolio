# DVD Bulk Deletion Script

import psycopg2

# Connection details
connection = psycopg2.connect(
    database="your_database",
    user="your_username",
    password="your_password", # Replace with your actual password
    host="your_host",
    port="your_port"
)

cursor = connection.cursor()

try:
    # --- OPTION A: The Range (e.g., Delete everything from ID 11 to 18) ---
    # start_id = 11
    # end_id = 18
    # delete_query = "DELETE FROM dvds WHERE film_id BETWEEN %s AND %s;"
    # params = (start_id, end_id)

    # --- OPTION B: The Shopping List (Specific IDs like 2, 4, 7) ---
    # Just put the IDs you want to get rid of inside the brackets below:
    target_ids = (11, 12, 13) 
    delete_query = "DELETE FROM dvds WHERE film_id IN %s;"
    params = (target_ids,) 

    # Execute the command
    cursor.execute(delete_query, params)
    
    # Commit the changes to the database
    connection.commit()
    
    print("------------------------------------------")
    print("BULK DELETE COMPLETE")
    print("The selected records have been removed.")
    print("------------------------------------------")

except Exception as error:
    print(f"Error: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
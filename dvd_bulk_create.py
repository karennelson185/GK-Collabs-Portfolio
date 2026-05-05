# DVD Bulk Creation Script 


import psycopg2

# Order: Title, Director, Actor, Actress, Genre, Media, Cert, Runtime, Year
dvd_list = [
    ('', '', '', '', '', '', '', , ),
    ('', '', '', '', '', '', '', , ),
    ('', '', '', '', '', '', '', , )
]

try:
    connection = psycopg2.connect(
        user="your_username",
        password="your_password", 
        host="your_host", 
        port="your_port",
        database="your_database"
    )
    cursor = connection.cursor()

    # Added lead_actress to the headers here
    insert_query = """ 
        INSERT INTO dvds (title, director, lead_actor, lead_actress, genre, media_source, certification, runtime, release_year) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
    """

    cursor.executemany(insert_query, dvd_list)
    connection.commit()
    print(f"Success! {cursor.rowcount} films added to the database.")

except Exception as error:
    print("Connection Error:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
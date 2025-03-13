import sqlite3

# Connect to the database
conn = sqlite3.connect("the.db")
cursor = conn.cursor()


def tee_table():

    table = """
    CREATE TABLE jokes(
    id INTEGER PRIMARY KEY,
    setup VARCHAR(255) NOT NULL,
    punch VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    times_seen INTEGER
    )
"""


    cursor.execute(table)




def käyläpi_jokes():
    # Fetch all rows from the jokes table
    cursor.execute("SELECT * from jokes")

    rows = cursor.fetchall()  # Get all results

    lista = []
    # Print each row
    for row in rows:
        setupin_eka_kirjain = row[1][0:3]
        if setupin_eka_kirjain == "Why":
            print(row)


    # Close the connection
    conn.close()


def lisää_jokes():

    cursor.execute("INSERT INTO jokes(setup, punch) VALUES('höpö','söpö')")
    conn.commit()
    











if __name__ == "__main__":
    käyläpi_jokes()


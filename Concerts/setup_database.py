import sqlite3

def setup_database():
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    # Read and execute the initial migration script
    with open('migration.sql', 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

    # Read and execute the concerts migration script
    with open('concerts_migration.sql', 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    setup_database()
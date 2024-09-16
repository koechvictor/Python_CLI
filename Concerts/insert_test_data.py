import sqlite3

def insert_test_data():
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO bands (name, hometown) VALUES (?, ?)', ('Band1', 'Hometown1'))
    cursor.execute('INSERT INTO bands (name, hometown) VALUES (?, ?)', ('Band2', 'Hometown2'))

    cursor.execute('INSERT INTO venues (title, city) VALUES (?, ?)', ('Venue1', 'City1'))
    cursor.execute('INSERT INTO venues (title, city) VALUES (?, ?)', ('Venue2', 'City2'))

    cursor.execute('INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)', (1, 1, '2023-10-01'))
    cursor.execute('INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)', (2, 2, '2023-11-01'))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    insert_test_data()
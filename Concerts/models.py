import sqlite3

class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @staticmethod
    def band(concert_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT bands.id, bands.name, bands.hometown
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.id = ?
        ''', (concert_id,))
        band = cursor.fetchone()
        connection.close()
        return band

    @staticmethod
    def venue(concert_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT venues.id, venues.title, venues.city
            FROM concerts
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        ''', (concert_id,))
        venue = cursor.fetchone()
        connection.close()
        return venue

    @staticmethod
    def hometown_show(concert_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        ''', (concert_id,))
        result = cursor.fetchone()
        connection.close()
        return result[0] == result[1]

    @staticmethod
    def introduction(concert_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT bands.name, bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        ''', (concert_id,))
        result = cursor.fetchone()
        connection.close()
        return f"Hello {result[2]}!!!!! We are {result[0]} and we're from {result[1]}"

class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    @staticmethod
    def concerts(venue_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT concerts.id, concerts.band_id, concerts.venue_id, concerts.date
            FROM concerts
            WHERE concerts.venue_id = ?
        ''', (venue_id,))
        concerts = cursor.fetchall()
        connection.close()
        return concerts

    @staticmethod
    def bands(venue_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT DISTINCT bands.id, bands.name, bands.hometown
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.venue_id = ?
        ''', (venue_id,))
        bands = cursor.fetchall()
        connection.close()
        return bands

    @staticmethod
    def concert_on(venue_id, date):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT concerts.id, concerts.band_id, concerts.venue_id, concerts.date
            FROM concerts
            WHERE concerts.venue_id = ? AND concerts.date = ?
            LIMIT 1
        ''', (venue_id, date))
        concert = cursor.fetchone()
        connection.close()
        return concert

    @staticmethod
    def most_frequent_band(venue_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT bands.id, bands.name, bands.hometown, COUNT(concerts.id) as concert_count
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.venue_id = ?
            GROUP BY bands.id
            ORDER BY concert_count DESC
            LIMIT 1
        ''', (venue_id,))
        band = cursor.fetchone()
        connection.close()
        return band

class Band:
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

    @staticmethod
    def concerts(band_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT concerts.id, concerts.band_id, concerts.venue_id, concerts.date
            FROM concerts
            WHERE concerts.band_id = ?
        ''', (band_id,))
        concerts = cursor.fetchall()
        connection.close()
        return concerts

    @staticmethod
    def venues(band_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT DISTINCT venues.id, venues.title, venues.city
            FROM concerts
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.band_id = ?
        ''', (band_id,))
        venues = cursor.fetchall()
        connection.close()
        return venues

    @staticmethod
    def play_in_venue(band_id, venue_title, date):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT id FROM venues WHERE title = ?
        ''', (venue_title,))
        venue_id = cursor.fetchone()[0]
        cursor.execute('''
            INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)
        ''', (band_id, venue_id, date))
        connection.commit()
        connection.close()

    @staticmethod
    def all_introductions(band_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT bands.name, bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.band_id = ?
        ''', (band_id,))
        results = cursor.fetchall()
        connection.close()
        introductions = [f"Hello {result[2]}!!!!! We are {result[0]} and we're from {result[1]}" for result in results]
        return introductions

    @staticmethod
    def most_performances():
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT bands.id, bands.name, bands.hometown, COUNT(concerts.id) as concert_count
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            GROUP BY bands.id
            ORDER BY concert_count DESC
            LIMIT 1
        ''')
        band = cursor.fetchone()
        connection.close()
        return band
import csv
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# Drop tables if they exist to start fresh
cur.executescript('''
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)
''')

# Read data from tracks.csv and insert into the database
filename = input("Enter file name: ")
if len(filename) < 1: filename = 'tracks.csv'

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        artist_name = row['Artist']
        album_title = row['Album']
        track_title = row['Name']
        genre_name = row['Genre']
        len_value = row['Time']
        rating_value = row['Rating']
        count_value = row['Count']
        
        # Insert or ignore artist
        cur.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES (?)''', (artist_name,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist_name,))
        artist_id = cur.fetchone()[0]
        
        # Insert or ignore album
        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES (?, ?)''', (album_title, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album_title,))
        album_id = cur.fetchone()[0]
        
        # Insert or ignore genre
        cur.execute('''INSERT OR IGNORE INTO Genre (name) 
            VALUES (?)''', (genre_name,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
        genre_id = cur.fetchone()[0]
        
        # Insert track
        cur.execute('''INSERT INTO Track (title, album_id, genre_id, len, rating, count) 
            VALUES (?, ?, ?, ?, ?, ?)''', (track_title, album_id, genre_id, len_value, rating_value, count_value))

# Commit changes to the database
conn.commit()

# Execute the provided query
cur.execute('''
SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
''')

# Print the results
print("Query Results:")
for row in cur.fetchall():
    print(row)

# Close the database connection
cur.close()

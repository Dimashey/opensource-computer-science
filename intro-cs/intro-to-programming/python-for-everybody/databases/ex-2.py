import sqlite3
import xml.etree.ElementTree as ET

connection = sqlite3.connect("musical-track.sqlite")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Artist")
cursor.execute("DROP TABLE IF EXISTS Genre")
cursor.execute("DROP TABLE IF EXISTS Album")
cursor.execute("DROP TABLE IF EXISTS Track")

cursor.execute("CREATE TABLE Artist ( id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name    TEXT UNIQUE)")
cursor.execute("CREATE TABLE Genre ( id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name    TEXT UNIQUE)")
cursor.execute("CREATE TABLE Album ( id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT UNIQUE)")
cursor.execute("CREATE TABLE Track ( id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT  UNIQUE, album_id  INTEGER, genre_id  INTEGER, len INTEGER, rating INTEGER, count INTEGER)")

tree = ET.parse('Library.xml')

root = tree.getroot()

data = root.findall('dict/dict/dict')

def get_artist_id(artist_name):
    cursor.execute('SELECT id FROM Artist WHERE name = ? ', (artist_name, ))
    artist_id = cursor.fetchone()[0]

    return artist_id

def get_album_id(album_name):
    cursor.execute('SELECT id FROM Album WHERE title = ? ', (album_name, ))
    album_id = cursor.fetchone()[0]

    return album_id

def get_genre_id(genre_name):
    cursor.execute('SELECT id FROM Genre WHERE name = ? ', (genre_name, ))
    genre_id = cursor.fetchone()[0]

    return genre_id


def get_field_value(key, items):
    found = False
    for child in items:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

for items in data:
    track_name = get_field_value('Name', items)
    play_count = get_field_value('Play Count', items)
    rating = get_field_value('Rating', items)
    genre_name = get_field_value('Genre', items)
    artist_name = get_field_value('Artist', items)
    album_name = get_field_value('Album', items)
    length = get_field_value('Total Time', items)

    if artist_name is None or genre_name is None or album_name is None:
        continue

    cursor.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist_name, ))
    cursor.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre_name, ))

    artist_id = get_artist_id(artist_name)

    cursor.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )', ( album_name, artist_id ) )

    album_id = get_album_id(album_name)
    genre_id = get_genre_id(genre_name)
    cursor.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, genre_id, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( track_name, album_id, length, genre_id, rating, play_count ) )

    connection.commit()
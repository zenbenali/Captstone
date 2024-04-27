import json
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()

# Drop tables if they exist to start fresh
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Load JSON data from file
filename = 'roster_data.json'
data = open(filename).read()
json_data = json.loads(data)

# Populate User and Course tables
for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # Insert or ignore user
    cur.execute('''INSERT OR IGNORE INTO User (name) 
        VALUES (?)''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Insert or ignore course
    cur.execute('''INSERT OR IGNORE INTO Course (title) 
        VALUES (?)''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert member with role
    cur.execute('''INSERT INTO Member (user_id, course_id, role) 
        VALUES (?, ?, ?)''', (user_id, course_id, role))

# Commit changes to the database
conn.commit()

# Execute the provided SQL commands
cur.execute('''
SELECT User.name, Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2
''')

print("Query 1 Results:")
for row in cur.fetchall():
    print('|'.join(map(str, row)))

cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1
''')

print("\nQuery 2 Results:")
for row in cur.fetchall():
    print(row[0])

# Close the database connection
cur.close()

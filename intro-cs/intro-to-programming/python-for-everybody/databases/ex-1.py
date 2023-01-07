import sqlite3
import urllib.request

connection = sqlite3.connect('counting-organisation.sqlite')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Counts")
cursor.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

file_handle = urllib.request.urlopen('http://data.pr4e.org/mbox.txt')

def get_domain(email): 
    return email.split('@')[1]

def get_email(line):
    return line.split()[1]

for line in file_handle:
    converted_line = line.decode().strip()
    if not converted_line.startswith('From '): continue
    email = get_email(converted_line)
    domain = get_domain(email)

    cursor.execute("SELECT count FROM Counts WHERE org = ? ", (domain,))
    row = cursor.fetchone()

    if row is None:
        cursor.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))

connection.commit()

connection.close()

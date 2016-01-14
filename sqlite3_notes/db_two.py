import sqlite3

conn = sqlite3.connect('music.sqlite')
cur  = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',
    ( 'gOD IS NOT DEAD', 34) )
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',
    ( 'all the my savior leads me', 33) )

conn.commit()

print("Accessing the Tracks table")
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)

cur.close()

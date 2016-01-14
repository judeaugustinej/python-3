""" Creating a table called Tracks,
in database music.sqlite, with columns
as title and plays.
"""
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur  = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks ')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()

import sqlite3

def connect():
    conn = sqlite3.connect('data.db')
    return conn


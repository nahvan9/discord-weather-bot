import sqlite3


def initializeDB(dbfile):
    conn = None
    try:
        conn = sqlite3.connect(dbfile)
        return conn
    except sqlite3.Error as e:
        return conn, e

def createTable(conn, description):
    userTable_description = """CREATE TABLE IF NOT EXISTS users(
                            id INT PRIMARY KEY NOT NULL, 
                            discordID TEXT NOT NULL, 
                            location TEXT NOT NULL
                        );"""
    userTableCol = "(discordID, location)"
    conn.execute(userTable_description)
    
    return userTableCol



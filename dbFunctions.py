import sqlite3


def create(dbfile):
    conn = None
    
    try:
        conn = sqlite3.connect(dbfile)
        return conn
    except sqlite3.Error as e:
        return conn, e
    
def createTable(conn, description):
    # Check if table exists:
    tableName = description.rsplit('(')[0].rsplit(' ')[-1]
    tableInfo = conn.execute(f"PRAGMA table_info({tableName})").fetchall()
    if len(tableInfo)>0:
        tableColumns = [a[1] for a in tableInfo]
        return tableName, tableColumns
    else:
        conn.execute(description)
        tableColumns = [a[1] for a in conn.execute(f"PRAGMA table_info({tableName})").fetchall()]
        return tableName, tableColumns
    

if __name__ == "__main__":
    d = create('.\\db\\test2.db')
    exampleTable = """CREATE TABLE IF NOT EXISTS users( 
                            discordID TEXT NOT NULL, 
                            location TEXT NOT NULL
                        );"""
    table = createTable(d, exampleTable)
    print(table)
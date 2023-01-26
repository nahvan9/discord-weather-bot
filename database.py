import os
import pathlib
import sqlite3


from utils import chkDir


class Database():
    def __init__(self, dbPath, initializer):
        self.path = dbPath
        self.init = initializer
        self.tableName = self.init.rsplit('(')[0].rsplit(' ')[-1]
        
        path = pathlib.Path(self.path)
        chkDir(path.parent.absolute())
        
        self.conn = self._initializeDB()
        
        if type(self.conn) == str:
            self.tableInfo = None
            self.tableCol = None
            self.tableColSet = None
            print(self.conn)
        else:
            self.tableInfo = self.conn.execute(f"PRAGMA table_info({self.tableName})")
            self.tableCol = [a[1] for a in self.tableInfo.fetchall()]
            self.tableColSet = ", ".join(str(s) for s in self.tableCol)
            
            
    def _initializeDB(self):
        conn = None
        try:
            conn = sqlite3.connect(self.path)
            conn.execute(self.init)
            return conn
        except sqlite3.Error as e:
            return e
    
    def _openDB(self):
        self.conn = sqlite3.connect(self.path)
        return self.conn
    
    def _closeDB(self):
        self.conn.close()
        self.conn = None
    
    def addEntry(self, values, tableName=None):
        # values: 'value1, value2, value3, etc'
        # tableName 'tableName (col1, col2, col3)'
        
        if self.conn != None:
            if tableName != None:
                self.conn.execute(f"INSERT INTO {tableName} VALUES ({values})")
            else:
                self.conn.execute(f"INSERT INTO {self.tableName} ({self.tableColSet}) VALUES ({values})")
            return True
        else:
            return False
    
    def modEntry(self, set, whereProp, whereVal):
        #set: "name = 'joe', id = 213, property = 'asd'"
        if self.conn != None:
            self.conn.execute(f"UPDATE {self.tableName} SET {set} WHERE {whereProp} = {whereVal}")
            return True
        else:
            return False
    
    def delEntry(self, whereProp, whereVal):
        if self.conn != None:
            self.conn.execute(f"DELETE FROM {self.tableName} WHERE {whereProp} = {whereVal}")
            return True
        else:
            return False
        
    def getEntry(self, select, whereProp, whereVal):
        #select: "name, id"
        if self.conn != None:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT {select} FROM {self.tableName} WHERE {whereProp} = {whereVal}")
            return cursor.fetchall()
        else:
            return False
    
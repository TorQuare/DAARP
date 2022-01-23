import pymysql as mysql

class SQL:

    dbName = ""
    cursor = None
    con = None

    def __init__(self, hostName, userName, password, newDbName):
        self.dbName=newDbName

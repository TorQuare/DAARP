import pyodbc
import os

class AC_database():

    path = ""
    cursor = None
    con = None

    def __init__(self, dbName):
        print(os.getcwd())
        self.path = os.getcwd()+"\\"+dbName
        full_path = self.path.rstrip()
        print(full_path)
        for i in pyodbc.drivers():
            print(i)

        #self.con = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+self.path+";")
        #self.con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Lenovo\PycharmProjects\DAARP_AfterExam\Test_2.accdb;')
        #self.cursor = self.con.cursor()
        print("work")
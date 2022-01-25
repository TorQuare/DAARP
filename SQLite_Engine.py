import os
import sqlite3
import sys
import Reader


class SQLite():
    path = ""
    con = None
    cursor = None
    Error_log = Reader.Reader_ERROR()

    def __init__(self, db_name):
        self.path = os.getcwd() + "\\" + db_name
        full_path = self.path.rstrip()
        try:
            self.con = sqlite3.connect(full_path)
            self.cursor = self.con.cursor()
        except:
            self.cursor = None
            exc_type, exc_obj, exc_tb = sys.exc_info()
            self.Error_log.Create_new_log("No connection to SQLite: " + str(exc_obj) + " " + str(exc_tb.tb_lineno))
            SQLite.close_conn(self)

    def create_tables(self):
        iterator = 0
        query_Users = "CREATE TABLE IF NOT EXISTS Users (ID integer PRIMARY KEY AUTOINCREMENT, Name text NOT NULL, " \
                      "Password text NOT NULL, Emg_question text NOT NULL, Emg_answer text NOT NULL, " \
                      "Last_login_date numeric NOT NULL, Type text NOT NULL, Second_ID integer NOT NULL, " \
                      "FOREIGN KEY (Type) REFERENCES User_type(Type));"
        query_Media = "CREATE TABLE IF NOT EXISTS Media (ID integer PRIMARY KEY AUTOINCREMENT, " \
                      "User_ID integer NOT NULL, Login text NOT NULL, Password text NOT NULL, " \
                      "Name text NOT NULL, Address text NOT NULL, Last_remind_date numeric, " \
                      "Remind_acc integer, Autorun_select text NOT NULL, Type text NOT NULL, " \
                      "FOREIGN KEY (User_ID) REFERENCES Users(ID), FOREIGN KEY (Type) REFERENCES Media_type(Type));"
        query_Media_type = "CREATE TABLE IF NOT EXISTS Media_type (ID integer PRIMARY KEY AUTOINCREMENT, " \
                           "Type text NOT NULL);"
        query_User_type = "CREATE TABLE IF NOT EXISTS User_type (ID integer PRIMARY KEY AUTOINCREMENT, " \
                          "Type text NOT NULL);"

        query = [["query_Media_type", query_Media_type], ["query_User_type", query_User_type],
                 ["query_Users", query_Users], ["query_Media", query_Media]]

        try:
            for i in query:
                if self.cursor:
                    self.cursor.execute(query[iterator][1])
                    self.con.commit()
                    iterator += 1
            SQLite.insert_default_types(self)
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            self.Error_log.Create_new_log("SQLite table: " + str(exc_obj) + " " + str(exc_tb.tb_lineno))

    def insert_default_types(self):
        table_name = [["User_type", "Administrator", "Normal"], ["Media_type", "APP", "WEB"]]
        iterator_name = 0
        iterator = 1
        try:
            for dt in table_name:
                query_del = "DELETE FROM `"+table_name[iterator_name][0]+"`"
                if self.cursor:
                    self.cursor.execute(query_del)
                    self.con.commit()
                iterator_name += 1
            iterator_name = 0
            for i in table_name:
                for i in table_name:
                    query_insert = "INSERT INTO `"+table_name[iterator_name][0]
                    query_insert += "`( `Type`) VALUES ('" + table_name[iterator_name][iterator] + "')"
                    if self.cursor:
                        self.cursor.execute(query_insert)
                        self.con.commit()
                    iterator += 1
                iterator = 1
                iterator_name += 1
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            self.Error_log.Create_new_log("SQLite default: " + str(exc_obj) + " " + str(exc_tb.tb_lineno))

    def create_default_admin_acc(self):
        query = "INSERT INTO Users"

    def close_conn(self):
        if self.con:
            self.con.close()
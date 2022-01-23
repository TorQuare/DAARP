import sqlite3
import os
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
        except sqlite3.Error as e:
            self.cursor = None
            self.Error_log.Create_new_log("No connection to SQLite: "+str(e))
            SQLite.close_conn(self)

    def create_tables(self):
        query_names = ["query_Media_type", "query_User_type", "query_Users", "query_Media"]
        iterator = 0
        query_Users = "CREATE TABLE IF NOT EXISTS Users (ID integer PRIMARY KEY AUTOINCREMENT, Name text NOT NULL, " \
                      "Password text NOT NULL, Emg_question text NOT NULL, Emg_answer text NOT NULL, " \
                      "Last_login_date numeric NOT NULL, Type text NOT NULL, Second_ID integer NOT NULL" \
                      "FOREIGN KEY (Type) REFERENCES User_type(Type));"
        query_Media = "CREATE TABLE IF NOT EXISTS Media (ID integer PRIMARY KEY AUTOINCREMENT, " \
                      "User_ID integer NOT NULL, Login text NOT NULL, Password text NOT NULL" \
                      "Name text NOT NULL, Address text NOT NULL, Last_remind_date numeric, " \
                      "Remind_acc integer, Autorun_select text NOT NULL, Type text NOT NULL," \
                      "FOREIGN KEY (User_ID) REFERENCES Users(ID), FOREIGN KEY (Type) REFERENCES Media_type(Type));"
        query_Media_type = "CREATE TABLE IF NOT EXISTS Media_type (ID integer PRIMARY KEY AUTOINCREMENT, " \
                           "Type text NOT NULL);"
        query_User_type = "CREATE TABLE IF NOT EXISTS User_type (ID integer PRIMARY KEY AUTOINCREMENT, " \
                          "Type text NOT NULL);"
        for i in query_names:
            if self.cursor:
                self.cursor.execute(query_names[iterator])
                self.con.commit()
                iterator+=1

    def insert_default(self):
        user_type = ["Administrator", "Normal"]
        iterator = 0
        try:
            for i in user_type:
                query_user_type = "INSERT INTO `User_type`( `Type`) VALUES ('"+user_type[iterator]+"')"
                iterator+=1
                if self.cursor:
                    self.cursor.execute(query_user_type)
                    self.con.commit()
        except sqlite3.Error as e:
            self.Error_log.Create_new_log("SQLite default: "+str(e))


    def close_conn(self):
        if self.con:
            self.con.close()
            print("con_close")

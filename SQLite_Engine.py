import os
import sqlite3
import Reader
import Crypto_Engine
import datetime
import Query_Builder


class SQLiteEngine:
    path = ""
    con = None
    cursor = None
    Error_log = Reader.ReaderERROR()
    UserCrypto = Crypto_Engine.UserCrypto()

    def __init__(self, db_name=None):
        self.query = Query_Builder.Builder(True)
        if db_name:
            SQLiteEngine.con_cursor_creator(self, db_name)

    def con_cursor_creator(self, db_name):
        self.path = os.getcwd() + "\\" + db_name
        full_path = self.path.rstrip()
        try:
            self.con = sqlite3.connect(full_path)
            self.cursor = self.con.cursor()
        except:
            self.cursor = None
            self.Error_log.create_new_log("No connection to SQLite")
            SQLiteEngine.close_conn(self)

    def select_user_data(self):
        val = []
        vals = "asb"
        for i in range(9):
            val.append("'" + vals + str(i) + "'")
        print(len(val))
        # result = SQLiteEngine.query_creator(1, 0, val)
        result = self.query.query_creator(1, 0, val)

    def close_conn(self):
        if self.con:
            self.con.close()


class SQLDefaultCreation(SQLiteEngine):

    def run_creator(self):
        try:
            SQLDefaultCreation.create_tables(self)
            SQLDefaultCreation.insert_default_types(self)
            SQLDefaultCreation.create_default_admin_acc(self)
            SQLDefaultCreation.close_conn(self)
        except:
            self.cursor = None
            self.Error_log.create_new_log("Creator")
            SQLDefaultCreation.close_conn(self)

    def create_tables(self):
        iterator = 0
        query_users = "CREATE TABLE IF NOT EXISTS Users (ID integer PRIMARY KEY AUTOINCREMENT, " \
                      "Name text NOT NULL UNIQUE, Password text NOT NULL, Emg_question text NOT NULL, " \
                      "Emg_answer text NOT NULL, Create_date text NOT NULL, Last_login_date text NOT NULL, " \
                      "Type text NOT NULL, Second_ID integer NOT NULL, FOREIGN KEY (Type) REFERENCES User_type(Type));"
        query_media = "CREATE TABLE IF NOT EXISTS Media (ID integer PRIMARY KEY AUTOINCREMENT, " \
                      "User_ID integer NOT NULL, Login text NOT NULL, Password text NOT NULL, " \
                      "Name text NOT NULL, Address text NOT NULL, Last_remind_date numeric, " \
                      "Remind_acc integer, Autorun_select text NOT NULL, Type text NOT NULL, " \
                      "FOREIGN KEY (User_ID) REFERENCES Users(ID), FOREIGN KEY (Type) REFERENCES Media_type(Type));"
        query_media_type = "CREATE TABLE IF NOT EXISTS Media_type (ID integer PRIMARY KEY AUTOINCREMENT, " \
                           "Type text NOT NULL UNIQUE);"
        query_user_type = "CREATE TABLE IF NOT EXISTS User_type (ID integer PRIMARY KEY AUTOINCREMENT, " \
                          "Type text NOT NULL UNIQUE);"

        query = [["query_media_type", query_media_type], ["query_user_type", query_user_type],
                 ["query_users", query_users], ["query_media", query_media]]

        try:
            for i in query:
                if self.cursor:
                    self.cursor.execute(query[iterator][1])
                    self.con.commit()
                    iterator += 1
            SQLDefaultCreation.insert_default_types(self)
        except:
            self.Error_log.create_new_log("SQLite table")

    def insert_default_types(self):
        table_name = [["User_type", "Administrator", "Normal"], ["Media_type", "APP", "WEB"]]
        iterator_name = 0
        iterator = 1
        try:
            for dt in table_name:
                query_del = "DELETE FROM `" + table_name[iterator_name][0] + "`"
                if self.cursor:
                    self.cursor.execute(query_del)
                    self.con.commit()
                iterator_name += 1
            iterator_name = 0
            for i in table_name:
                for j in table_name:
                    query_insert = "INSERT INTO `" + table_name[iterator_name][0]
                    query_insert += "`( `Type`) VALUES ('" + table_name[iterator_name][iterator] + "')"
                    if self.cursor:
                        self.cursor.execute(query_insert)
                        self.con.commit()
                    iterator += 1
                iterator = 1
                iterator_name += 1
        except:
            self.Error_log.create_new_log("SQLite default")

    def create_default_admin_acc(self):
        query = "INSERT INTO `Users` ( `Name`, `Password`, `Emg_question`, `Emg_answer`, " \
                "`Create_date`, `Last_login_date`, `Type`, `Second_ID`) VALUES ( "
        query_second_id = "11111"
        query_value_enc_log = self.UserCrypto.pass_crypto_mode_hash("Administrator")
        query_value_emg = self.UserCrypto.aes_block_mode(True, query_second_id, "Emergency")
        date = datetime.datetime.now()  # zapis daty 02/11/22
        # date = datetime.date.today()  # alternatywny zapis daty 2022-02-11
        today = date.strftime("%x")
        today_time = date.strftime("%x %X")
        try:
            query += "'" + query_value_enc_log + "', '" + query_value_enc_log + "', '" + query_value_emg + \
                     "', '" + query_value_emg + "', '" + str(today) + \
                     "', '" + str(today_time) + "', 'Administrator', " + query_second_id + ")"
            if self.cursor:
                self.cursor.execute(query)
                self.con.commit()
        except:
            self.Error_log.create_new_log("SQLite default")
            SQLDefaultCreation.manual_delete(self)

    def manual_delete(self):
        query = "DELETE FROM `Users`"
        if self.cursor:
            self.cursor.execute(query)
            self.con.commit()
            print("MANUAL DELETE")

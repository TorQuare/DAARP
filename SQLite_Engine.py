import os
import sqlite3
import Reader
import Crypto_Engine
import datetime


class SQLiteEngine:
    path = ""
    con = None
    cursor = None
    Error_log = Reader.ReaderERROR()
    UserCrypto = Crypto_Engine.UserCrypto()
    users_row_names = ["ID", "Name", "Password",
                       "Emg_question", "Emg_answer",
                       "Create_date", "Last_login_date",
                       "Type", "Second_ID"]

    def __init__(self, db_name):
        self.path = os.getcwd() + "\\" + db_name
        full_path = self.path.rstrip()
        try:
            self.con = sqlite3.connect(full_path)
            self.cursor = self.con.cursor()
        except:
            self.cursor = None
            self.Error_log.create_new_log("No connection to SQLite")
            SQLiteEngine.close_conn(self)

    @staticmethod
    def query_creator(query_id, table_id, values, split_method):
        query = ["SELECT * FROM", "INSERT INTO", "DELETE FROM", "WHERE", "VALUES"]
        table_values = [
            " Users", " Media", [
                "ID", "Name", "Password",
                "Emg_question", "Emg_answer",
                "Create_date", "Last_login_date",
                "Type", "Second_ID"
            ], [
                "ID", "User_ID", "Login",
                "Password", "Name", "Address",
                "Last_remind_date", "Remind_acc",
                "Autorun_select", "Type"
            ]
        ]
        values_arr = values.split(split_method)
        result = ""
        result += query[query_id] + table_values[table_id] + " ( "
        table_id += 2
        print(len(table_values[table_id]), "  ", len(values_arr))
        print(table_values[table_id])
        for i in table_values[table_id]:
            if len(values_arr) == len(table_values[table_id]):
                if i == table_values[table_id][len(table_values[table_id])-1]:
                    result += i + ")"
                    break
                result += i + ", "
        print(result)
        return result

    def select_user_data(self):
        val = []
        vals = ""
        for i in range(8):
            vals += "asb"
        vals += "fas"
        result = SQLiteEngine.query_creator(1, 0, vals)

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

import json
import configparser
# import Crypto
import datetime
import sys


class CreateDefault:

    def __init__(self, switch):     # tworzenie domyślnego pliku ini
        if switch == "INI":
            CreateDefault.create_ini()
        if switch == "JSON":
            CreateDefault.create_json()
        if switch == "ERROR":
            CreateDefault.create_error()

    @staticmethod
    def create_ini():
        config = configparser.ConfigParser()
        config.add_section("basic_config")
        config.set("basic_config", "stay_logged", "False")
        config.set("basic_config", "keep_login", "False")
        config.set("basic_config", "default_database", "True")
        config.set("basic_config", "database_view", "Full_mode")

        config.add_section("last_values")
        config.set("last_values", "last_login", "None")
        config.set("last_values", "last_database", "Default")

        config_file = open("config.ini", 'w')
        config.write(config_file)
        config_file.close()

    @staticmethod
    def create_json():
        default = {
            "List": [
                {
                    "Type": "Local",
                    "Name": "Default",
                    "Additional_name": "Default",
                    "User_name": "Default",
                    "Password": "Default",
                    "Ip": "127.0.0.1"
                },
                {
                    "Type": "Online",
                    "Name": "Test_1",
                    "Additional_name": "Test_1",
                    "User_name": "Tester",
                    "Password": "Default",
                    "Ip": "123.0.0.2"
                }
            ]
        }
        with open("data.json", 'w') as json_file:
            json.dump(default, json_file)

    @staticmethod
    def create_error():
        actual_date = datetime.datetime.now()
        file = open("ERROR_Logs.txt", 'w')
        file.write(str(actual_date)+" Log list created!\n")
        for i in range(120):
            file.write("-")
        file.close()


class ReaderERROR:

    actual_date = datetime.datetime.now()
    file_name = "ERROR_Logs.txt"

    def __init__(self):
        try:
            file = open(self.file_name, 'r')
            file.close()
        except:
            CreateDefault("ERROR")

    def create_new_log(self, file):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(exc_obj, " ", exc_tb.tb_lineno)
        log = file + ": " + str(exc_obj) + " " + str(exc_tb.tb_lineno)
        file = open(self.file_name, 'a')
        file.write("\n"+str(self.actual_date)+"\n")
        file.write(log+"\n")
        for i in range(60):
            file.write("-")
        file.close()


class ReaderINI:

    config = configparser.ConfigParser()
    file_name = "config.ini"

    def __init__(self):     # sprawdzanie czy istnieją pliki configuracyjne i czy są zgodne
        self.basic_config = "basic_config"
        self.last_values = "last_values"
        self.stay_logged = "stay_logged"
        self.keep_login = "keep_login"
        self.default_database = "default_database"
        self.database_view = "database_view"
        self.last_login = "last_login"
        self.last_database = "last_database"
        self.value_true = "True"
        self.value_false = "False"
        try:
            config_file = open(self.file_name, 'r')
            config_file.close()
            self.config.read(self.file_name)
            basic_value = self.config.get(self.basic_config, self.stay_logged)
            basic_value = self.config.get(self.basic_config, self.keep_login)
            basic_value = self.config.get(self.basic_config, self.default_database)
            basic_value = self.config.get(self.basic_config, self.database_view)
            basic_value = self.config.get(self.last_values, self.last_login)
            basic_value = self.config.get(self.last_values, self.last_database)
        except:
            CreateDefault("INI")

    def check_stay_logged(self):
        self.config.read(self.file_name)
        if self.config.get(self.basic_config, self.stay_logged) == self.value_true:
            return True
        if self.config.get(self.basic_config, self.stay_logged) == self.value_false:
            return False

    def check_keep_login(self):
        self.config.read(self.file_name)
        if self.config.get(self.basic_config, self.keep_login) == self.value_true:
            return True
        if self.config.get(self.basic_config, self.keep_login) == self.value_false:
            return False

    def check_default_database(self):
        self.config.read(self.file_name)
        if self.config.get(self.basic_config, self.default_database) == self.value_true:
            return True
        if self.config.get(self.basic_config, self.default_database) == self.value_false:
            return False

    def check_last_login(self):
        self.config.read(self.file_name)
        return self.config.get(self.last_values, self.last_login)

    def check_last_database(self):
        self.config.read(self.file_name)
        return self.config.get(self.last_values, self.last_database)

    def database_view_mode(self):
        self.config.read(self.file_name)
        return self.config.get(self.basic_config, self.database_view)

    def update_basic_config(self, node, value):
        set_value = ""
        if value:
            set_value = self.value_true
        if not value:
            set_value = self.value_false
        self.config.set(self.basic_config, node, set_value)
        config_file = open(self.file_name, 'w')
        self.config.write(config_file)
        config_file.close()

    # TO DO: dodać funkcje wyciągania z pliku loginu i bazy danych - zaszyfrować te dane jeżeli nie są default


class ReaderJSON:

    file_name = "data.json"

    def __init__(self):
        self.list = "List"
        self.type = "Type"
        self.name = "Name"
        self.additional_name = "Additional_name"
        self.user_name = "User_name"
        self.password = "Password"
        self.ip = "Ip"
        with open(self.file_name, 'r') as json_file:
            self.config_file = json.load(json_file)
        try:
            config_file = open(self.file_name, 'r')
            config_file.close()
            default_value = self.config_file[self.list][0][self.type]
            default_value = self.config_file[self.list][0][self.name]
            default_value = self.config_file[self.list][0][self.additional_name]
            default_value = self.config_file[self.list][0][self.user_name]
            default_value = self.config_file[self.list][0][self.password]
            default_value = self.config_file[self.list][0][self.ip]
        except:
            CreateDefault("JSON")

    def database_list(self, switch):
        iterator = 0
        name_tab = []
        full_name = ""
        name_mode = "Name_mode"
        ip_mode = "Ip_mode"
        full_mode = "Full_mode"
        for i in self.config_file[self.list]:
            name = self.config_file[self.list][iterator][self.additional_name]
            ip = self.config_file[self.list][iterator][self.ip]
            index = iterator+1
            if switch == name_mode:
                full_name = str(index)+". "+name
            if switch == ip_mode:
                full_name = str(index)+". ("+ip+")"
            if switch == full_mode:
                full_name = str(index)+"."+name+" ("+ip+")"
            name_tab.append(full_name)
            iterator += 1
        return name_tab

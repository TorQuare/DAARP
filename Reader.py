import json
import configparser
import Crypto
import datetime

class Create_default:

    def __init__(self, switch):     #tworzenie domyślnego pliku ini
        if switch == "INI":
            Create_default.Create_INI(self)
        if switch == "JSON":
            Create_default.Create_JSON(self)
        if switch == "ERROR":
            Create_default.Create_ERROR(self)


    def Create_INI(self):
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

    def Create_JSON(self):
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

    def Create_ERROR(self):
        actual_date = datetime.datetime.now()
        file = open("ERROR_Logs.txt", 'w')
        file.write(str(actual_date)+" Log list created!\n")
        for i in range(120):
            file.write("-")
        file.close()

class Reader_ERROR:

    actual_date = datetime.datetime.now()

    def __init__(self):
        try:
            file = open("ERROR_Logs.txt", 'r')
            file.close()
        except:
            Create_default.__init__(self, "ERROR")

    def Create_new_log(self, log):
        file = open("ERROR_Logs.txt", 'a')
        file.write("\n"+str(self.actual_date)+"\n")
        file.write(log+"\n")
        for i in range(60):
            file.write("-")
        file.close()

class Reader_INI:

    config = configparser.ConfigParser()

    def __init__(self):     #sprawdzanie czy istnieją pliki configuracyjne i czy są zgodne
        try:
            config_file = open("config.ini", 'r')
            config_file.close()
            self.config.read("config.ini")
            basic_value = self.config.get("basic_config", "stay_logged")
            basic_value = self.config.get("basic_config", "keep_login")
            basic_value = self.config.get("basic_config", "default_database")
            basic_value = self.config.get("basic_config", "database_view")
            basic_value = self.config.get("last_values", "last_login")
            basic_value = self.config.get("last_values", "last_database")
        except:
            Create_default.__init__(self, "INI")

    def Check_stay_logged(self):
        self.config.read("config.ini")
        if self.config.get("basic_config", "stay_logged")=="True":
            return True
        if self.config.get("basic_config", "stay_logged")=="False":
            return False

    def Check_keep_login(self):
        self.config.read("config.ini")
        if self.config.get("basic_config", "keep_login")=="True":
            return True
        if self.config.get("basic_config", "keep_login")=="False":
            return False

    def Check_default_database(self):
        self.config.read("config.ini")
        if self.config.get("basic_config", "default_database")=="True":
            return True
        if self.config.get("basic_config", "default_database")=="False":
            return False

    def Check_last_login(self):
        self.config.read("config.ini")
        return self.config.get("last_values", "last_login")

    def Check_last_database(self):
        self.config.read("config.ini")
        return self.config.get("last_values", "last_database")

    def Database_view_mode(self):
        self.config.read("config.ini")
        return self.config.get("basic_config", "database_view")

    def Update_basic_config(self, node, value):
        if value==True:
            set_value="True"
        if value==False:
            set_value="False"
        self.config.set("basic_config", node, set_value)
        config_file = open("config.ini", 'w')
        self.config.write(config_file)
        config_file.close()

    #TO DO: dodać funkcje wyciągania z pliku loginu i bazy danych - zaszyfrować te dane jeżeli nie są default

class Reader_JSON:

    def __init__(self):
        with open("data.json", 'r') as json_file:
            self.config_file = json.load(json_file)
        try:
            config_file = open("data.json", 'r')
            config_file.close()
            default_value = self.config_file["List"][0]["Type"]
            default_value = self.config_file["List"][0]["Name"]
            default_value = self.config_file["List"][0]["Additional_name"]
            default_value = self.config_file["List"][0]["User_name"]
            default_value = self.config_file["List"][0]["Password"]
            default_value = self.config_file["List"][0]["Ip"]
        except:
            Create_default.__init__(self, "JSON")

    def Database_list(self, switch):
        iterator = 0
        name_tab = []
        for i in self.config_file["List"]:
            name = self.config_file["List"][iterator]["Additional_name"]
            ip = self.config_file["List"][iterator]["Ip"]
            index = iterator+1
            if switch == "Name_mode":
                full_name = str(index)+". "+name
            if switch == "Ip_mode":
                full_name = str(index)+". ("+ip+")"
            if switch == "Full_mode":
                full_name = str(index)+"."+name+" ("+ip+")"
            name_tab.append(full_name)
            iterator+=1
        return name_tab
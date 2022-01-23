import Reader

class selector:

    def __init__(self):
        self.Reader_JSON = Reader.Reader_JSON()
        self.Reader_INI = Reader.Reader_INI()

    def Database_select(self):
        Last_select_name = self.Reader_INI.Check_last_database()
        iterator = 0
        if Last_select_name=="Default":
            return 0
        for i in self.Reader_JSON.Database_list("Name_mode"):
            name = self.Reader_JSON.config_file["List"][iterator]["Additional_name"]
            if name==Last_select_name:
                return iterator
            iterator+=1

import Reader


class Selector:

    def __init__(self):
        self.ReaderJSON = Reader.ReaderJSON()
        self.ReaderINI = Reader.ReaderINI()
        self.list = "List"
        self.default = "Default"
        self.additional_name = "Additional_name"

    def database_select(self):
        last_select_name = self.ReaderINI.check_last_database()
        name_mode = "Name_mode"
        iterator = 0
        if last_select_name == self.default:
            return 0
        for i in self.ReaderJSON.database_list(name_mode):
            name = self.ReaderJSON.config_file[self.list][iterator][self.additional_name]
            if name == last_select_name:
                return iterator
            iterator += 1

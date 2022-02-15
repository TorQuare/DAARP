class Builder:

    def __init__(self, sql_mode):
        if sql_mode:
            self.query = ["SELECT * FROM ", "INSERT INTO ", "DELETE FROM ", ") WHERE ( ", ") VALUES ( "]
            self.table_values = [
                "Users ( ", "Media ( ",
                [
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

    def query_creator(self, query_id, table_id, values):
        result = ""
        result += self.query[query_id] + self.table_values[table_id]
        table_id += 2
        print(len(self.table_values[table_id]), "  ", len(values))
        for i in self.table_values[table_id]:
            if len(values) == len(self.table_values[table_id]):
                if i == self.table_values[table_id][len(self.table_values[table_id])-1]:
                    result += i
                    break
                result += i + ", "
        if query_id == 1:
            result += self.query[4]
            for i in values:
                if len(values) == len(self.table_values[table_id]):
                    if i == values[len(values) - 1]:
                        result += i + ")"
                        break
                    result += i + ", "
        print(result)
        return result

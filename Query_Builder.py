class Builder:

    def __init__(self, sql_mode):
        if sql_mode:
            self.query = ["SELECT * FROM ", "INSERT INTO ", "DELETE FROM ", ") WHERE ( ", ") VALUES ( "]
            self.sign = [" ( ", ") ", "'", ", "]
            self.table_values = [
                "Users", "Media",
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

    def query_builder(self, select_mode, insert_mode, user_table, values):
        adv_mode = False
        result = ""
        if user_table:
            table_id = 0
        else:
            table_id = 1
        values_arr = Builder.add_quote(self, values)
        if select_mode:
            query_id = 0
            sec_query_id = 3
        elif insert_mode:
            query_id = 1
            sec_query_id = 4
        elif not select_mode and not insert_mode:
            query_id = 2
            sec_query_id = 3
        else:
            return False
        if len(values) < len(self.table_values[table_id+2])-1:
            adv_mode = True
        if adv_mode:
            result = Builder.query_adv_creator(self)
        elif not adv_mode:
            result = Builder.query_basic_creator(self, self.query[query_id], table_id,
                                                 values_arr, self.query[sec_query_id])
        return result

    def add_quote(self, values):
        iterator = 0
        for i in values:
            if i.isnumeric():
                values[iterator] = i
            else:
                values[iterator] = self.sign[2] + i + self.sign[2]
            iterator += 1
        return values

    def query_basic_creator(self, pre_query, table_id, values, selector):
        result = pre_query
        result += self.table_values[table_id] + self.sign[0]
        table_id += 2
        iterator = 0
        for i in values:
            if len(values) == len(self.table_values[table_id]):
                result += self.table_values[table_id][iterator] + self.sign[3]
            else:
                if iterator > 0:
                    result += self.table_values[table_id][iterator] + self.sign[3]
            iterator += 1
            if iterator == len(values)-1:
                result += self.table_values[table_id][iterator]
                break
        result += selector
        for i in values:
            if i == values[len(values)-1]:
                result += i + self.sign[1]
                break
            result += i + self.sign[3]
        print(result)
        return result

    def query_adv_creator(self):

        return None

import pymysql as mysql  # ładowanie biblioteki
import sys
import msvcrt
import hashlib
from tkinter import messagebox

class SQL(object):

    ver = 1.0
    dbName = ""
    cursor = None
    con = None
    now= None
    u_id= None

    def __init__(self, hostName, userName, password, newDbName):
        self.dbName = newDbName
        try:
            self.con = mysql.connect(host=hostName, user=userName, passwd=password, db=self.dbName)
            self.cursor = self.con.cursor()
            if(self.con):
                print(self.con)
            else:
                messagebox.showerror("DB Error!", "Błąd łączenia z bazą!")
            print(self.cursor)
        except NameError:
            self.cursor = None
            messagebox.showerror("DB Error", "Błędna baza danych!")
        except ValueError as exp:
            self.cursor = None
            messagebox.showerror("No NET", "Brak internetu!")
        except Exception as exp:
            self.cursor = None
            messagebox.showerror("DB Error", "Baza nie działa!")

        # łączenie się z bazą danych
        # tworzy obiekt,którym będzie można wysyłać zapytania do bazy danych


    def AddUser(self, login, haslo, Security, SecurityPass):
        query = "INSERT INTO `user`( `Name`, `Pass`, `Security`, `SecurityPass`)"
        query += " VALUES ('" + login + "', '" + haslo + "', '"+ Security +"', '"+ SecurityPass +"')"
        print(query)
        result = None
        if(self.cursor):
            result = self.cursor.execute(query)
            self.con.commit()
            print (result)
            messagebox.showinfo("Gratulacje!", "Pomyślne utworzono!") #do edycji na statusbar
        else:
            messagebox.showinfo("Error!", "Błędne dane!")
        return result

    def newPass(self, oldpas, newpas, option, secPasUpdate, secQ):
        query = "SELECT `Name` FROM `user` WHERE Pass = '" + oldpas + "' AND Log = 1 "
        result = None
        if(self.cursor):
            result = self.cursor.execute(query)
            self.con.commit()
            if(result==1):
                dbName = ""
                Name = ""
                for record in self.cursor:
                    Name = dbName.join(record)
                if(option=="Normal"):
                    return SQL.trueReset(self, Name, newpas)
                elif(option=="Security"):
                    return SQL.trueSecReset(self, Name, secPasUpdate, secQ)
            else:
                return False
        else:
            return False

    def trueReset(self, login, haslo):
        query = "UPDATE user SET Pass = '"+ haslo +"' WHERE Name = '"+login+"'"
        #result = None
        if(self.cursor):
            #result = self.cursor.execute(query)
            self.cursor.execute(query)
            self.con.commit()
            return True
        else:
            return False

    def trueSecReset(self, login, secpas, secQ):
        query = "UPDATE user SET SecurityPass = '"+ secpas +"' WHERE Name = '"+login+"'"
        queryQ = "UPDATE user SET Security = '"+ secQ +"' WHERE Name = '"+login+"'"
        result = None
        if(self.cursor):
            result = self.cursor.execute(query)
            self.con.commit()
            if(result==1):
                self.cursor.execute(queryQ)
                self.con.commit()
                return True
            else:
                return False
        else:
            return False

    def check(self, login):
        query = "SELECT * FROM user WHERE Name = '" + login + "'"
        queryPass = "SELECT Security FROM user WHERE Name = '" + login + "'"
        resultPass = None
        if(self.cursor):
            self.cursor.execute(query)
            self.con.commit()
            if(self.cursor):
                resultPass = self.cursor.execute(queryPass)
                self.con.commit()
                if(resultPass==0):
                    return False
                else:
                    pas = ""
                    for record in self.cursor:
                        return (pas.join(record))   #wyciąganie konkretnej wartości z tabeli
            else:
                return False
        else:
            return False
#^gotowe
    def reset(self, login, haslo, givenpas):
        haslo=SQL.check(self, login)
        query = "SELECT SecurityPass FROM user WHERE Name = '" + login + "' AND Security = '" + haslo + "'"
        result = None
        if (self.cursor):
            result = self.cursor.execute(query)
            self.con.commit()
            if(result==1):
                pasTake = ""
                pas = ""
                for record in self.cursor:
                    pas = (pasTake.join(record))
                if(pas==givenpas):  #sprawdzanie podanego hasła z hasłem bezpieczeństwa
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
#^gotowe
    def UrlNew(self, id_u, login, haslo, name, url, remind, r_date):
        if(remind=="NO_R"):
            query = "INSERT INTO `links` ( `ID_u`, `Login`, `Pass`, `Media`, `url`)"
            query += " VALUES ('" + id_u + "', '" + login + "','"+ haslo +"', '"+ name +"', '"+ url +"')"
        elif(remind=="YES_R"):
            query = "INSERT INTO `links` ( `ID_u`, `Login`, `Pass`, `Media`, `url`, `R_Date`)"
            query += " VALUES ('" + id_u + "', '" + login + "','" + haslo + "', '" + name + "', '" + url + "', '" + r_date + "')"
        if(self.cursor):
            self.cursor.execute(query)
            self.con.commit()
            return True
        else:
            return False
#^gotowe
    def AppNew(self, id_u, login, haslo, name, app, remind, r_date):
        if(remind=="NO_R"):
            query = "INSERT INTO `app` ( `ID_u`, `Login`, `Pass`, `Media`, `app`)"
            query += " VALUES ('" + id_u + "', '" + login + "','"+ haslo +"', '"+ name +"', '"+ app +"')"
        elif(remind=="YES_R"):
            query = "INSERT INTO `app` ( `ID_u`, `Login`, `Pass`, `Media`, `app`, `R_Date`)"
            query += " VALUES ('" + id_u + "', '" + login + "','" + haslo + "', '" + name + "', '" + app + "', '" + r_date + "')"
        if(self.cursor):
            self.cursor.execute(query)
            self.con.commit()
            return True
        else:
            return False
#^gotowe
    def AutorunAdd(self, id_u, name, adress):
        query = "INSERT INTO `autorun` ( `ID_u`, `Media`, `Adress`)"
        query += " VALUES ('" + id_u + "', '" + name + "', '" + adress + "')"
        if(self.cursor):
            self.cursor.execute(query)
            self.con.commit()
            return True
        else:
            return False
#^gotowe
    def UrlDel(self, id_u, name):
        queryURL = "DELETE FROM links WHERE `ID_u`=" + id_u + " AND `Media`='" + name + "'"
        queryAPP = "DELETE FROM app WHERE `ID_u`=" + id_u + " AND `Media`='" + name + "'"
        queryAuto = "DELETE FROM autorun WHERE `ID_u`=" + id_u + " AND `Media`='" + name + "'"
        result = None
        if(self.cursor):
            result = self.cursor.execute(queryURL)
            self.con.commit()
            if(result==1):
                self.cursor.execute(queryAuto)
                self.con.commit()
                return True
            else:
                result = self.cursor.execute(queryAPP)
                self.con.commit()
                if(result==1):
                    self.cursor.execute(queryAuto)
                    self.con.commit()
                    return True
                else:
                    return False
        else:
            messagebox.showerror("Error!", "Error!")
#^gotowe

    def UrlEdit(self, id_u, login, haslo, name, url):
        query = "UPDATE `links` SET `Login` = '"+login+"', `Pass` = '"+haslo+"', `Media` = '"+name+"', `url` = '"+url+"'"
        query += "WHERE `ID_u`="+id_u+" AND `Media`='"+name+"'"
        print(query)
        result = None
        if(self.cursor):
            result = self.cursor.execute(query)
            self.con.commit()
            messagebox.showinfo("Zakończono!", "Pomyślnie edytowano link")
        else:
            messagebox.showerror("Error!", "Błąd danych!")
        return result

    def login(self, login, password):
        query = "SELECT * FROM user WHERE Name = '" + login + "' AND Pass = '" + password + "'"
        queryCl = "UPDATE user SET Log = '0'"
        queryLog = "UPDATE user SET Log = '1' WHERE user.Name = '"+ login +"'"
        result = None
        resultCl = None
        resultLog = None
        if(self.cursor):
            result = self.cursor.execute(query)
            self.con.commit()
            if (result==1):
                resultCl = self.cursor.execute(queryCl)
                self.con.commit()
                resultCl = 1
                if(resultCl==1):
                    resultLog = self.cursor.execute(queryLog)
                    self.con.commit()
                    if(resultLog==1):
                        return True
            else:
                self.cursor.execute(queryCl)
                self.con.commit()
                return False
        else:
            return False

    def login2(self, log):
        query = "SELECT * FROM user WHERE Log = '"+log+"'"
        result = None
        if(self.cursor):
            result = self.cursor.execute(query)
            self.con.commit()
            if (result==1):
                for record in self.cursor:
                    return record
            else:
                return result

    def check_pass(self, log, pas):
        query = "SELECT * FROM user WHERE Log = '"+log+"' AND Pass = '" + pas + "'"
        result = None
        if(self.cursor):
            result = self.cursor.execute(query)
            self.con.commit()
            if(result==1):
                return True
            else:
                return False

    def ExMaker(self, id_u, login, pas, media, url, select):
        queryURL = "SELECT * FROM links WHERE ID_u = '" + id_u + "'"
        queryAPP = "SELECT * FROM app WHERE ID_u = '" + id_u + "'"
        exampleQueryURL = "INSERT INTO `links` ( `ID_u`, `Login`, `Pass`, `Media`, `url`)"
        exampleQueryURL += " VALUES ('" + id_u + "', '" + login + "','" + pas + "', '" + media + "', '" + url + "')"
        exampleQueryAPP = "INSERT INTO `app` ( `ID_u`, `Login`, `Pass`, `Media`, `app`)"
        exampleQueryAPP += " VALUES ('" + id_u + "', '" + login + "','" + pas + "', '" + media + "', '" + url + "')"
        resultURL = None
        resultAPP = None
        if (self.cursor):  # tworzenie example sprawdzając od URL
            resultURL = self.cursor.execute(queryURL)
            self.con.commit()
            print(resultURL, select, "EXStep1")
            if (resultURL == 0 and select=="URL"):
                self.cursor.execute(exampleQueryURL)
                self.con.commit()

        if (self.cursor):  # tworzenie example sprawdzając od APP
            resultAPP = self.cursor.execute(queryAPP)
            self.con.commit()
            print(resultAPP, select, "EXStep1")
            if (resultAPP == 0 and select=="APP"):
                self.cursor.execute(exampleQueryAPP)
                self.con.commit()

    def mediaAll(self, id_u):
        queryURL = "SELECT * FROM links WHERE ID_u = '" + id_u + "'"
        queryAPP = "SELECT * FROM app WHERE ID_u = '" + id_u + "'"
        resultURL = None
        resultAPP = None
        tab = []
        inde = 0
        if(self.cursor):        #wyciąganie wartości z links
            resultURL = self.cursor.execute(queryURL)
            self.con.commit()
            if(resultAPP!=0):
                for record in self.cursor:
                    tab.append(inde)
                    tab[inde]= str(record[4])
                    inde = inde + 1
                    print(tab, "url")
            else:
                return None

        if(self.cursor):        #wyciąganie wartości z app
            resultAPP = self.cursor.execute(queryAPP)
            self.con.commit()
            if(resultAPP!=0):
                for record in self.cursor:
                    tab.append(inde)
                    tab[inde] = str(record[4])
                    inde = inde + 1
                    print(tab, "app")
            else:
                return None
        return tab

    def mediaSelect(self, id_u, select):
        if(select=="URL"):
            query = "SELECT * FROM links WHERE ID_u = '" + id_u + "'"
        elif(select=="APP"):
            query = "SELECT * FROM app WHERE ID_u = '" + id_u + "'"
        tab = []
        inde = 0
        if (self.cursor):
            self.cursor.execute(query)
            self.con.commit()
            for record in self.cursor:
                tab.append(inde)
                tab[inde] = str(record[4])
                inde = inde + 1
                print(tab, "select")
            return tab
        else:
            return None

    def mediaAutorun(self, id_u):
        query = "SELECT * FROM autorun WHERE ID_u = '" + id_u + "'"
        tab = []
        inde = 0
        if (self.cursor):
            self.cursor.execute(query)
            self.con.commit()
            for record in self.cursor:
                tab.append(inde)
                tab[inde] = str(record[2])
                inde = inde + 1
                print(tab, "autorun")
            return tab
        else:
            return None

    def url(self, id_u, nazwa):
        query = "SELECT * FROM links WHERE ID_u = '" + id_u + "' AND Media = '"+ nazwa +"'"
        result = None
        if(self.cursor):
            result = self.cursor.execute(query)
            self.con.commit()
            if (result==0):
                return None
            else:
                for record in self.cursor:
                    return record
        else:
            return None

    def app(self, id_u, nazwa):
        query = "SELECT * FROM app WHERE ID_u = '" + id_u + "' AND Media = '"+ nazwa +"'"
        result = None
        if(self.cursor):
            result = self.cursor.execute(query)
            self.con.commit()
            if (result==0):
                return None
            else:
                for record in self.cursor:
                    return record
        else:
            return None

    def __del__(self):
        if(self.cursor is not None):
            self.cursor.close() #zerwanie połączenia z bazą danych

    def logout(self):
        queryCl = "UPDATE user SET Log = '0'"
        self.cursor.execute(queryCl)
        self.con.commit()   #wylogowanie po zamknięciu programu (4up)


#sql.AddUser('Patryk','Patryk')
#id_u=sql.login2('Patryk', 'Patryk')

#if(id):
 #   sql.media(id_u)
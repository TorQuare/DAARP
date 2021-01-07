from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import simpledialog
import passql
import Anubis
import os
import webbrowser
from threading import Timer

DAA = Anubis.Anubis()
sql = passql.SQL('127.0.0.1', 'root', '', 'test')
dataLog = sql.login2('1')

def AutorunTimer():
    config = Timer(2, Autorun)
    config.start()

def Autorun():
    lista = sql.mediaAutorun(str(dataLog[0]))
    for line in lista:
        url = sql.url(str(dataLog[0]), DAA.AES_Enc(line))
        app = sql.app(str(dataLog[0]), DAA.AES_Enc(line))


def Bind_mouse_listbox_doubleclic(self):
    run()

def run():
    checked=Anubis.Anubis.From_list(Lb2.get(ACTIVE))
    url = sql.url(str(dataLog[0]), DAA.AES_Enc(checked))
    app = sql.app(str(dataLog[0]), DAA.AES_Enc(checked))
    val_list = val.get()
    if(val_list==1):
        if(url!=0 and url!=None):
            try:
                webbrowser.open(DAA.AES_Dec(str(url[5])))
            except:
                messagebox.showerror("ERROR!", "STRING ERROR!")
        elif(app!=0 and app!=None):
            try:
                os.system(DAA.AES_Dec(str(app[5])))
            except:
                messagebox.showerror("ERROR!", "STRING ERROR!")
    elif(val_list==2):
        try:
            webbrowser.open(DAA.AES_Dec(str(url[5])))
        except:
            messagebox.showerror("ERROR!", "STRING ERROR!")
    elif(val_list==3):
        try:
            os.system(DAA.AES_Dec(str(app[5])))
        except:
            messagebox.showerror("ERROR!", "STRING ERROR!")


def Bind_mouse_lsitbox_rightclick(self):
    logPass()

def logPass():

    def check_pas(lockPas):     #sprawdzanie podanego hasła z bazą
        pas = str(lockPas)
        check = sql.check_pass(str(dataLog[0]), Anubis.Anubis.MD5_Hash(pas))
        if(check==True):
            pas_value.set(DAA.AES_Dec(url[3]))
            pasButton.destroy()
            pasLabel = Label(show, textvariable=pas_value)
            pasLabel.grid(row=2, column=3)

        else:
            messagebox.showerror("Błąd!", "Błędne hasło")

    def show_pass():        #okno sprawdzające hasło
        def close():
            showPas.destroy()
        def close_check():
            check_pas(lockPas.get())
            close()
        showPas = Toplevel(show)
        showPas.title("Lock")
        showPas.geometry("194x90")
        Label(showPas, text=" ").grid(row=0, column=0)
        Label(showPas, text="Podaj hasło\ndo programu:").grid(row=1, column=1)
        lockPas = Entry(showPas, show="*", width=15)
        lockPas.grid(row=1, column=2)
        Button(showPas, image=wht, text="OK", height=20, width=67, command=close_check, compound="center").grid(row=2, column=1)
        Button(showPas, image=wht, text="Anuluj", height=20, width=67, command=close, compound="center").grid(row=2, column=2)

    login_value = StringVar()
    login_value.set("...")
    pas_value = StringVar()
    pas_value.set("...")
    adres_value = StringVar()
    adres_value.set("...")
    name_value = StringVar()
    name_value.set("...")
    date_value = StringVar()
    date_value.set("...")
    checked=Anubis.Anubis.From_list(Lb2.get(ACTIVE))
    urlSQL = sql.url(str(dataLog[0]), DAA.AES_Enc(checked))
    appSQL = sql.app(str(dataLog[0]), DAA.AES_Enc(checked))

    if (urlSQL!=0 and urlSQL!=None):        #sprawdzanie czy to aplikacja czy strona
        url = sql.url(str(dataLog[0]), DAA.AES_Enc(checked))
    elif (appSQL!=0 and appSQL!=None):
        url = sql.app(str(dataLog[0]), DAA.AES_Enc(checked))
    else:
        messagebox.showerror("ERROR!", "STRING ERROR!")

    try:
        login_value.set(DAA.AES_Dec(url[2]))
        pas_value.set("Pokaż")
        name_value.set(DAA.AES_Dec(url[4]))
        adresLen = len(DAA.AES_Dec(url[5]))
        if(adresLen<=15):
            adres_value.set(DAA.AES_Dec(url[5]))
        else:
            new_adres_value = DAA.AES_Dec(url[5])[:14]+"..."
            adres_value.set(new_adres_value)
        if(url[6]!=None and url[6]!=0):
            date_value.set(DAA.AES_Dec(url[6]))
        else:
            date_value.set("N/D")
    except:
        messagebox.showerror("ERROR!", "STRING ERROR!")

    show = Toplevel(logman)
    show.title("Szczegóły")
    show.geometry("205x155")
    Label(show, text="Login:").grid(row=1, column=1)
    Label(show, text="Hasło:").grid(row=2, column=1)
    Label(show, text="Adres:").grid(row=3, column=1)
    Label(show, text="Nazwa:").grid(row=4, column=1)
    Label(show, text="Data\nprzypomnienia:").grid(row=5, column=1)
    login = Label(show, textvariable=login_value)
    login.grid(row=1, column=3)
    pasButton = Button(show, textvariable=pas_value, command=show_pass, compound="center")
    pasButton.grid(row=2, column=3, columnspan=2)
    adres = Label(show, textvariable=adres_value)
    adres.grid(row=3, column=3)
    name = Label(show, textvariable=name_value)
    name.grid(row=4, column=3)
    date = Label(show, textvariable=date_value)
    date.grid(row=5, column=3)
    Button(show, image=wht, text="Edytuj", height=20, width=67, compound="center").grid(row=6, column=2, columnspan=3, sticky=W)
    Label(show, text=" ").grid(row=7, column=0)

def urlnewWindow():
    os.system('C:\\Users\Lenovo\PycharmProjects\DAARPv3\Daarp_add_url.py')
    Lb2.delete(0, END)
    loadmedia()

def delUrl():
    checked=Anubis.Anubis.From_list(Lb2.get(ACTIVE))
    sql.UrlDel(str(dataLog[0]), DAA.AES_Enc(checked))
    sql.UrlDel(str(dataLog[0]), checked)
    Lb2.delete(0, END)
    loadmedia()

def ListChose():
    if(val.get()==4):
        runButton.config(state=DISABLED)
    else:
        runButton.config(state=NORMAL)
    Lb2.delete(0, END)
    loadmedia()

def NewPasWindow():
    def newPass():
        actPas = a1.get()
        actPasHash = Anubis.Anubis.MD5_Hash(actPas)
        newPas = r1.get()
        newPasHash = Anubis.Anubis.MD5_Hash(newPas)
        newPasVer = r2.get()
        if (newPas == newPasVer):
            status = sql.newPass(actPasHash, newPasHash, "Normal", "", "")
            if (status == True):
                messagebox.showinfo("Gratulacje!", "Ustawiono nowe hasło!")
                destroyPass()
            else:
                messagebox.showerror("Błąd!", "Podane hasło jest niepoprawne!")
        else:
            messagebox.showerror("Błąd!", "Podane hasła nie są identyczne!")

    def destroyPass():
        newPas.destroy()

    newPas = Toplevel(logman)
    newPas.title("Reset hasła")
    newPas.geometry("220x120")
    Label(newPas, text="Aktualne hasło", width="11").grid(row=1, column=0)
    Label(newPas, text="Nowe hasło", width="11").grid(row=2, column=0)
    Label(newPas, text="Powtórz nowe\nhasło", width="11").grid(row=3, column=0)
    a1 = Entry(newPas, show="*")
    a1.grid(row=1, column=1)
    r1 = Entry(newPas, show="*")
    r1.grid(row=2, column=1)
    r2 = Entry(newPas, show="*")
    r2.grid(row=3, column=1)
    ok = Button(newPas, image=wht, text="Zatwierdź", height=20, width=67, command=newPass, compound="center")
    ok.grid(row=4, column=0)
    cancel = Button(newPas, image=wht, text="Anuluj", height=20, width=100, command=destroyPass, compound="center")
    cancel.grid(row=4, column=1)

def NewSecPasWindow():
    def newSecPass():
        actPas = a1.get()
        actPasHash = Anubis.Anubis.MD5_Hash(actPas)
        newPas = r1.get()
        newPasHash = Anubis.Anubis.MD5_Hash(newPas)
        newSec = Cbox.get()
        status = sql.newPass(actPasHash, "", "Security", newPasHash, newSec)
        if (status == True):
            messagebox.showinfo("Gratulacje!", "Ustawiono nowe hasło bezpieczeństwa!")
            destroySecPass()
        else:
            messagebox.showerror("Błąd!", "Podane hasło jest niepoprawne!")

    def destroySecPass():
        newPas.destroy()

    newPas = Toplevel(logman)
    newPas.title("Reset hasła")
    newPas.geometry("220x200")
    Label(newPas, text="Hasło do konta:", width="11").pack(side=TOP)
    a1 = Entry(newPas, show="*")
    a1.pack(side=TOP)
    Label(newPas, text="Wybierz hasło\nbezpieczeństwa:", width="11").pack(side=TOP)
    Cbox = ttk.Combobox(newPas, width=24)
    Cbox['values'] = ('Imię pierwszego zwierzaka',
                      'Miejsce urodzenia',
                      'Ulubione danie')
    Cbox.current(0)
    Cbox.pack(side=TOP)
    Label(newPas, text="Odpowiedź:", width="11").pack(side=TOP)
    r1 = Entry(newPas)
    r1.pack(side=TOP)
    ok = Button(newPas, image=wht, text="Zatwierdź", height=20, width=67, command=newSecPass, compound="center")
    ok.pack(side=TOP)
    cancel = Button(newPas, image=wht, text="Anuluj", height=20, width=100, command=destroySecPass, compound="center")
    cancel.pack(side=TOP)

def editUrl():
    return 0

def destroy():
    sql.logout()
    logman.destroy()

def logout():
    destroy()
    os.system('C:\\Users\Lenovo\PycharmProjects\DAARPv3\Pass_log.py')

logman = Tk()
logman.title("PassMan")
logman.geometry("270x250")
def on_close():
    sql.logout()
    logman.destroy()

menubar = Menu(logman)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Zmiana hasła", command=NewPasWindow)
filemenu.add_command(label="Zmiana pytania bezpieczeństwa", command=NewSecPasWindow)
filemenu.add_separator()
filemenu.add_command(label="Wyloguj", command=logout)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=destroy)
menubar.add_cascade(label="Plik", menu=filemenu)

configmenu = Menu(menubar, tearoff=0)
configmenu.add_command(label="Edycja linku")
configmenu.add_command(label="Ustawienia")
menubar.add_cascade(label="Edycja", menu=configmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Pomoc")
menubar.add_cascade(label="Pomoc", menu=helpmenu)

val = IntVar()
val.set('1')

Frame = LabelFrame(logman, text="Dzień dobry").pack()

Radiobutton(Frame, text="Wszystko", indicatoron=0, width=7, variable=val, bg="#cccccc", selectcolor="#e6f2ff", command=ListChose, value=1).place(x=7, y=10)
Radiobutton(Frame, text="Strony", indicatoron=0, width=7, variable=val, bg="#cccccc", selectcolor="#e6f2ff", command=ListChose, value=2).place(x=7, y=34)
Radiobutton(Frame, text="Aplikacje", indicatoron=0, width=7, variable=val, bg="#cccccc", selectcolor="#e6f2ff", command=ListChose,  value=3).place(x=7, y=58)
Radiobutton(Frame, text="Autorun", indicatoron=0, width=7, variable=val, bg="#cccccc", selectcolor="#e6f2ff", command=ListChose, value=4).place(x=7, y=82)

Lb2 = Listbox(Frame)

def loadmedia():
    checked = 0   #wybarana z listy nazwa
    number = 0
    val_list = val.get()   #odświeżanie listy
    if(val_list==1):
        lista = sql.mediaAll(str(dataLog[0]))
        if lista:
            checkURL = sql.mediaSelect(str(dataLog[0]), "URL")
            checkAPP = sql.mediaSelect(str(dataLog[0]), "APP")
            if not checkURL:
                lista = None
            if not checkAPP:
                lista = None
        print(lista, "val1")
    elif(val_list==2):
        lista = sql.mediaSelect(str(dataLog[0]), "URL")
        print(lista, "val2")
    elif(val_list==3):
        lista = sql.mediaSelect(str(dataLog[0]), "APP")
        print(lista, "val3")
    elif(val_list==4):
        lista = sql.mediaAutorun(str(dataLog[0]))
        print(lista, "val4")

    if lista:
        for line in lista:
            number+=1
            list_line = str(number)+"."+DAA.AES_Dec(line)
            Lb2.insert(checked, list_line)
            checked=checked+1
    elif(val_list!=4):
        sql.ExMaker(str(dataLog[0]), DAA.AES_Enc("ExampleLogin"), DAA.AES_Enc("ExamplePassword"), DAA.AES_Enc("ExampleSideName"), DAA.AES_Enc("https://www.google.pl/"), "URL")
        sql.ExMaker(str(dataLog[0]), DAA.AES_Enc("ExampleLogin"), DAA.AES_Enc("ExamplePassword"), DAA.AES_Enc("ExampleAppName"), DAA.AES_Enc("C:\WINDOWS\system32\mspaint.exe"), "APP")
        loadmedia()
    Lb2.place(x=62, y=10) #listbox z linkami

loadmedia()

wht = PhotoImage(file="pxwht.png")

runButton = Button(Frame, image=wht, text="Uruchom", height=20, width=67, command = run, compound="center")
runButton.place(x=190, y=10)
delUrl = Button(Frame, image=wht, text="Usuń adres", height=20, width=67, command = delUrl, compound="center")
delUrl.place(x=190, y=70)
addUrl = Button(Frame, image=wht, text="Dodaj", heigh=20, width=67, command = urlnewWindow, compound="center")
addUrl.place(x=190, y=40)
login = Button(Frame, image=wht, text="Wyświetl", height=20, width=67, command = logPass, compound="center")
login.place(x=190, y=120)

Lb2.bind('<Double-1>', Bind_mouse_listbox_doubleclic)
Lb2.bind('<Button-3>', Bind_mouse_lsitbox_rightclick)

statusbar = Label(logman, text="Zalogowany jako: "+dataLog[1], fg="black", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)
logman.protocol("WM_DELETE_WINDOW", on_close)
logman.config(menu=menubar)
logman.mainloop()
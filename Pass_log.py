from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import simpledialog
import passql
import os
import Anubis

sql = passql.SQL('127.0.0.1', 'root', '', 'test')


def Enter_press(self):
    log()

def log():
    log=e1.get()
    pas=e2.get()
    pasHash = Anubis.Anubis.MD5_Hash(pas)
    id_u = sql.login(log, pasHash)
    if(id_u==TRUE):
        messagebox.showinfo("Gratulacje!", "Pomyślne zalogowano!")
        paman.destroy()
        os.system('C:\\Users\Lenovo\PycharmProjects\DAARPv3\logman.py')
    else:
        messagebox.showerror("Error!", "Błędne dane!")

def addWindow():
    os.system('C:\\Users\Lenovo\PycharmProjects\DAARPv3\Daarp_user.py')

def restartWindow():
    os.system('C:\\Users\Lenovo\PycharmProjects\DAARPv3\Daarp_restart.py')

def configWindow():
    os.system('C:\\Users\Lenovo\PycharmProjects\DAARPv3\Daarp_config.py')

def destroy():
    sql.logout()
    paman.destroy()



paman = Tk()
paman.title("DAARP")
paman.geometry("200x100")
#paman.configure(background="black")
def on_close():
    sql.logout()
    paman.destroy()

paman.bind('<Return>', Enter_press)

menubar = Menu(paman)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nowy użytkownik", command=addWindow)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=destroy)
menubar.add_cascade(label="Plik", menu=filemenu)

configmenu = Menu(menubar, tearoff=0)
configmenu.add_command(label="Nowa baza", command=configWindow)
configmenu.add_command(label="Konfiguracja")
menubar.add_cascade(label="Konfiguracja", menu=configmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Pomoc")
menubar.add_cascade(label="Pomoc", menu=helpmenu)

wht = PhotoImage(file="pxwht.png")
Label(paman, text='Login').grid(row=0)
Label(paman, text='Hasło').grid(row=1)
e1 = Entry(paman)
e2 = Entry(paman, show="*")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
login = Button(paman, image=wht, text="Zaloguj", height=20, width=67, command=log, compound="center")
login.grid(row=3, column=0)
reset = Button(paman, image=wht, text="Reset hasła", height=20, width=67, command=restartWindow, compound="center")
reset.grid(row=3, column=1)
Label(paman, text='Wybór bazy:').grid(row=4)
Cbox = ttk.Combobox(paman, width=15)
Cbox['values'] = ('Imię pierwszego zwierzaka',
                  'Miejsce urodzenia',
                  'Ulubione danie')
Cbox.current(0)
Cbox.grid(row=4, column=1)
paman.protocol("WM_DELETE_WINDOW", on_close)
paman.config(menu=menubar)
paman.mainloop()
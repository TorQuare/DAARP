from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#from PIL import ImageTk,Image
from tkinter import simpledialog
import Reader
import Engine

class Logging_window:

    def __init__(self):
        self.Reader_JSON = Reader.Reader_JSON()
        self.Reader_INI = Reader.Reader_INI()
        self.Engine_selector = Engine.selector()
        self.keep_login = self.Reader_INI.Check_keep_login()
        self.stay_logged = self.Reader_INI.Check_stay_logged()
        self.default_database = self.Reader_INI.Check_default_database()
        self.last_database = self.Reader_INI.Check_last_database()
        self.last_login = self.Reader_INI.Check_last_login()
        self.database_view = self.Reader_INI.Database_view_mode()
        #self.sql = "alfa" passql.SQL('127.0.0.1', 'root', '', 'test')

    def update_keep_login(self):
        value = self.keep_login_new_value.get()
        node = "keep_login"
        self.Reader_INI.Update_basic_config(node, value)

    def Window(self):
        Window_one = Tk()
        Window_one.title("DAARP")
        Window_one.geometry("250x175")

        self.keep_login_new_value = BooleanVar()        #zmienna przechowująca wartość checkbuttonu

        #GUI paska menu
        Menubar = Menu(Window_one)
        Filemenu = Menu(Menubar, tearoff=0)
        Filemenu.add_command(label="Nowy użytkownik")
        Filemenu.add_command(label="Wyświetl bazy danych")
        Filemenu.add_separator()
        Filemenu.add_command(label="Ustawienia")
        Filemenu.add_separator()
        Filemenu.add_command(label="Exit")
        Menubar.add_cascade(label="Plik", menu=Filemenu)

        Configmenu = Menu(Menubar, tearoff=0)
        Configmenu.add_command(label="Nowa baza danych")
        Configmenu.add_command(label="Konfiguracja")
        Menubar.add_cascade(label="Konfiguracja", menu=Configmenu)

        Helpmenu = Menu(Menubar, tearoff=0)
        Helpmenu.add_command(label="Pomoc")
        Helpmenu.add_separator()
        Helpmenu.add_command(label="Panel administratora")
        Menubar.add_cascade(label="Pomoc", menu=Helpmenu)

        #GUI okna logowania
        Frame = LabelFrame(Window_one).pack()

        Label(Frame, text="Login").place(x=10, y=10)
        Label(Frame, text="Hasło").place(x=10, y=35)

        entry_login = Entry(Frame)
        entry_login.place(x=55, y=10)
        entry_password = Entry(Frame, show="*")
        entry_password.place(x=55, y=35)

        button_login = Button(Frame, text="Zaloguj")
        button_login.place(x=10, y=60)
        button_reset = Button(Frame, text="Reset hasła")
        button_reset.place(x=70, y=60)

        # checkbutton keep_login, stay_logged
        keep_login_checkbutton = Checkbutton(Frame, text="Zapamiętaj mnie", variable=self.keep_login_new_value,
                                             command=lambda: Logging_window.update_keep_login(self),
                                             onvalue=True, offvalue=False)
        keep_login_checkbutton.place(x=20, y=90)
        if self.keep_login==True:
            keep_login_checkbutton.select()
            entry_login.insert(0, self.Reader_INI.Check_last_login())

        # lista wyboru bazy
        Label(Frame, text="Wybór bazy:").place(x=10, y=120)

        base_select = ttk.Combobox(Frame)
        base_select['state'] = 'readonly'
        base_select['values'] = (self.Reader_JSON.Database_list(self.database_view))
        if self.default_database==True:
            base_select.current(0)
        else:
            base_select.current(self.Engine_selector.Database_select())
        base_select.place(x=80, y=120)

        #pasek stanu połączenia z bazą - dokończyć gdy będzie zrobione łączenie z bazą
        server_status = Label(Window_one, text="Status:", fg="black", bd=1, relief=SUNKEN, anchor=W)
        server_status.pack(side=BOTTOM, fill=X)

        Window_one.config(menu=Menubar)
        Window_one.mainloop()
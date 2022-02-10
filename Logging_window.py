from tkinter import *
# from tkinter import messagebox
from tkinter import ttk
# from PIL import ImageTk,Image
# from tkinter import simpledialog
import Reader
import Engine


class LoggingWindow:
    
    def __init__(self):
        self.ReaderJSON = Reader.ReaderJSON()
        self.ReaderINI = Reader.ReaderINI()
        self.Engine_selector = Engine.Selector()
        self.keep_login = self.ReaderINI.check_keep_login()
        self.stay_logged = self.ReaderINI.check_stay_logged()
        self.default_database = self.ReaderINI.check_default_database()
        self.last_database = self.ReaderINI.check_last_database()
        self.last_login = self.ReaderINI.check_last_login()
        self.database_view = self.ReaderINI.database_view_mode()
        # self.sql = "alfa" passql.SQL('127.0.0.1', 'root', '', 'test')

    def update_keep_login(self):
        value = self.keep_login_new_value.get()
        node = "keep_login"
        self.ReaderINI.update_basic_config(node, value)

    def window(self):
        window_one = Tk()
        window_one.title("DAARP")
        window_one.geometry("250x175")

        self.keep_login_new_value = BooleanVar()        # zmienna przechowująca wartość checkbuttonu

        # GUI paska menu
        menubar = Menu(window_one)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nowy użytkownik")
        filemenu.add_command(label="Wyświetl bazy danych")
        filemenu.add_separator()
        filemenu.add_command(label="Ustawienia")
        filemenu.add_separator()
        filemenu.add_command(label="Exit")
        menubar.add_cascade(label="Plik", menu=filemenu)

        configmenu = Menu(menubar, tearoff=0)
        configmenu.add_command(label="Nowa baza danych")
        configmenu.add_command(label="Konfiguracja")
        menubar.add_cascade(label="Konfiguracja", menu=configmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Pomoc")
        helpmenu.add_separator()
        helpmenu.add_command(label="Panel administratora")
        menubar.add_cascade(label="Pomoc", menu=helpmenu)

        # GUI okna logowania
        frame = LabelFrame(window_one).pack()

        Label(frame, text="Login").place(x=10, y=10)
        Label(frame, text="Hasło").place(x=10, y=35)

        entry_login = Entry(frame)
        entry_login.place(x=55, y=10)
        entry_password = Entry(frame, show="*")
        entry_password.place(x=55, y=35)

        button_login = Button(frame, text="Zaloguj")
        button_login.place(x=10, y=60)
        button_reset = Button(frame, text="Reset hasła")
        button_reset.place(x=70, y=60)

        # checkbutton keep_login, stay_logged
        keep_login_checkbutton = Checkbutton(frame, text="Zapamiętaj mnie", variable=self.keep_login_new_value,
                                             command=lambda: LoggingWindow.update_keep_login(self),
                                             onvalue=True, offvalue=False)
        keep_login_checkbutton.place(x=20, y=90)
        if self.keep_login:
            keep_login_checkbutton.select()
            entry_login.insert(0, self.ReaderINI.check_last_login())

        # lista wyboru bazy
        Label(frame, text="Wybór bazy:").place(x=10, y=120)

        base_select = ttk.Combobox(frame)
        base_select['state'] = 'readonly'
        base_select['values'] = (self.ReaderJSON.database_list(self.database_view))
        if self.default_database:
            base_select.current(0)
        else:
            base_select.current(self.Engine_selector.database_select())
        base_select.place(x=80, y=120)

        # pasek stanu połączenia z bazą - dokończyć gdy będzie zrobione łączenie z bazą
        server_status = Label(window_one, text="Status:", fg="black", bd=1, relief=SUNKEN, anchor=W)
        server_status.pack(side=BOTTOM, fill=X)

        window_one.config(menu=menubar)
        window_one.mainloop()

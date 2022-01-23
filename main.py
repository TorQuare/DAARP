import Logging_window
import Reader
import Engine
import ACCDB_Engine
import SQLite_Engine

Reader_INI = Reader.Reader_INI()    #sprawdzanie czy istnieją pliki configuracyjne i czy są zgodne
Reader_JSON = Reader.Reader_JSON()
#Reader.Create_default("ERROR")

SQLite = SQLite_Engine.SQLite("Default.db")
#SQLite.create_tables()
SQLite.insert_default()
SQLite.close_conn()

#Access = ACCDB_Engine.AC_database("Test_2.accdb")

Engine = Engine.selector()
Engine.Database_select()

Log_in = Logging_window.Logging_window()
Log_in.Window()

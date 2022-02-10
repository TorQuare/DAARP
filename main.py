import Logging_window
import Reader
import Engine
import SQLite_Engine
import Crypto_Engine

ReaderINI = Reader.ReaderINI()    # sprawdzanie czy istnieją pliki configuracyjne i czy są zgodne
ReaderJSON = Reader.ReaderJSON()
ReaderERROR = Reader.ReaderERROR()

SQLite = SQLite_Engine.SQLite("Default.db")
# SQLite.create_tables()
SQLite.close_conn()

UserCrypto = Crypto_Engine.UserCrypto()

Engine = Engine.Selector()
Engine.database_select()

Log_in = Logging_window.LoggingWindow()
Log_in.window()

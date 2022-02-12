import Logging_window
import Reader
import Engine
import SQLite_Engine
import Crypto_Engine

ReaderINI = Reader.ReaderINI()    # sprawdzanie czy istnieją pliki configuracyjne i czy są zgodne
ReaderJSON = Reader.ReaderJSON()
ReaderERROR = Reader.ReaderERROR()

SQLite = SQLite_Engine.SQLDefaultCreation("Default.db")
# SQLite.create_default_admin_acc()
# SQLite.create_tables()
SQLite.close_conn()

UserCrypto = Crypto_Engine.UserCrypto()
UserCrypto.code_gen()

Engine = Engine.Selector()
Engine.database_select()

Log_in = Logging_window.LoggingWindow()
Log_in.window()

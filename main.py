import Logging_window
import Reader
import Engine
import SQLite_Engine
import Crypto_Engine

ReaderINI = Reader.ReaderINI()    # sprawdzanie czy istnieją pliki configuracyjne i czy są zgodne
ReaderJSON = Reader.ReaderJSON()
ReaderERROR = Reader.ReaderERROR()

SQLite = SQLite_Engine.SQLDefaultCreation("Default.db")
# SQLite.run_creator()

UserCrypto = Crypto_Engine.UserCrypto()
MediaCrypto = Crypto_Engine.MediaCrypto()

Engine = Engine.Selector()
Engine.database_select()

Log_in = Logging_window.LoggingWindow()
Log_in.window()

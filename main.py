import Logging_window
import Reader
import Engine
import SQLite_Engine
import Crypto_Engine

Reader_INI = Reader.Reader_INI()    #sprawdzanie czy istnieją pliki configuracyjne i czy są zgodne
Reader_JSON = Reader.Reader_JSON()
Reader_ERROR = Reader.Reader_ERROR()

SQLite = SQLite_Engine.SQLite("Default.db")
#SQLite.create_tables()
SQLite.close_conn()

User_crypto = Crypto_Engine.User_crypto()
#User_crypto.Pass_crypto_mode_hash("Patryk")
User_crypto.EMG_question_AES_dec("Patryk", "4Y+fE93WI2ogW90U4OaQ9b2sIF998vSmaIeh5Ed6Ji4=")
#4Y+fE93WI2ogW90U4OaQ9b2sIF998vSmaIeh5Ed6Ji4=
#Ulubione zwierze?
Engine = Engine.selector()
Engine.Database_select()

Log_in = Logging_window.Logging_window()
Log_in.Window()

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
MediaCrypto.enc_string_generator(True, UserCrypto.code_gen(), "Mateusz", "Pa na toffffffffffffffffffffffffff af / 2156*")
# MediaCrypto.key_code_shaker(23383)
# MediaCrypto.enc_string_generator(False, 24679, "Mateusz", "llJ1K4MMcuGuTYehctnib7ksR1FNyyjNkU0P54adwYJvWqfpdBnboXrStoDADyiMZS0T0WNGjQw/VB4Z8Kiet94IBszklu2Bt9zmnexDLNKuwBNKNxdgYA==")
# MediaCrypto.aes_stream_mode(True, "5ba479b903e6a9dc5063b625ac33d723", "Patryk")
# MediaCrypto.aes_stream_mode(False, "5ba479b903e6a9dc5063b625ac33d722", "GTWamcoz")

Engine = Engine.Selector()
Engine.database_select()

Log_in = Logging_window.LoggingWindow()
Log_in.window()

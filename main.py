import Logging_window
import Reader
import Engine
import ACCDB_Engine

Reader_INI = Reader.Reader_INI()    #sprawdzanie czy istnieją pliki configuracyjne i czy są zgodne
#Reader_load.Check_stay_logged()     #zwraca wartość ustawienia flagi stay_logged
Reader_JSON = Reader.Reader_JSON()

Access = ACCDB_Engine.AC_database("Test_2.accdb")

Engine = Engine.selector()
Engine.Database_select()

Log_in = Logging_window.Logging_window()
Log_in.Window()

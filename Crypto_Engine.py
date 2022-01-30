import random
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256, SHA512
import base64
import hashlib
import Reader
import os
import sys

class User_crypto():
    Error_log = Reader.Reader_ERROR()

    def __init__(self):
        print("init")

    def Pass_crypto_mode_hash(self, string):
        try:
            S_512 = SHA512.new(data=string.encode('utf-8')).hexdigest()
            S_256 = SHA256.new(data=string.encode('utf-8')).hexdigest()
            User_crypto.MD5_code_return_only(self,S_256+S_512)
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            self.Error_log.Create_new_log("Crypto user: " + str(exc_obj) + " " + str(exc_tb.tb_lineno))


    def MD5_code_return_only(self, string):
        result = MD5.new(data=string.encode('utf-8')).hexdigest()
        return result

    def EMG_pass_crypto_mode_AES_enc(self, string):
        return 0

class Media_crypto():
    Error_log = Reader.Reader_ERROR()

    def __init__(self):
        print("init")
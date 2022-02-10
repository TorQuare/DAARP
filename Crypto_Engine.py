import random
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256, SHA512
from Crypto.Util import Padding
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
            User_crypto.MD5_code_return_only(self, S_256 + S_512)
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            self.Error_log.Create_new_log("Crypto user: " + str(exc_obj) + " " + str(exc_tb.tb_lineno))

    def MD5_code_return_only(self, string):
        result = MD5.new(data=string.encode('utf-8')).hexdigest()
        return result

    def Vector_for_AES(self, string):
        iterator = 0
        iv = ""
        check_if_int = string[0].isnumeric()
        if not check_if_int:
            for i in string:
                if iterator % 2 == 0:
                    iv += i
                iterator += 1
        else:
            for i in string:
                if 6 <= iterator <= 11:
                    iv += i
                if 19 <= iterator <= 28:
                    iv += i
                iterator += 1
        return iv.encode('utf-8')

    def EMG_question_AES_enc(self, encrypt, login, string):
        key = User_crypto.MD5_code_return_only(self, login).encode('utf-8')
        iv = User_crypto.Vector_for_AES(self, key.decode('utf-8'))
        cipher = AES.new(key, AES.MODE_CBC, iv)
        if encrypt:
            string_enc = Padding.pad(string.encode('utf-8'), 16)
            result = base64.b64encode(cipher.encrypt(string_enc)).decode('utf-8')
        #if not encrypt:
            #string_enc = Padding.unpad(string.encode('utf-8'), AES.block_size)
            #result = base64.b64decode(cipher.decrypt(string.encode)).decode('utf-8')
        print(result)

    def EMG_question_AES_dec(self, login, string):
        key = User_crypto.MD5_code_return_only(self, login).encode('utf-8')
        string_enc = Padding.pad(string.encode('utf-8'), AES.block_size)
        iv = User_crypto.Vector_for_AES(self, key.decode('utf-8'))
        new_key = base64.b64decode(key)
        string_new = base64.b64decode(string.encode('utf-8'))
        iv_new = base64.b64decode(iv)
        Encrypt = AES.new(key, AES.MODE_CBC, iv)
        result = Padding.unpad(Encrypt.encrypt(string.encode('utf-8')), 16).decode('utf-8')
        print(result)

class Media_crypto():
    Error_log = Reader.Reader_ERROR()

    def __init__(self):
        print("init")

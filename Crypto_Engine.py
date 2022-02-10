import random
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256, SHA512
from Crypto.Util import Padding
import base64
import Reader
import sys


class UserCrypto:
    Error_log = Reader.ReaderERROR()

    def __init__(self):
        print("init")

    def pass_crypto_mode_hash(self, string):
        try:
            sha_512 = SHA512.new(data=string.encode('utf-8')).hexdigest()
            sha_256 = SHA256.new(data=string.encode('utf-8')).hexdigest()
            UserCrypto.md5_code_return_only(sha_256 + sha_512)
        except SyntaxError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            self.Error_log.create_new_log("Crypto user: " + str(exc_obj) + " " + str(exc_tb.tb_lineno))

    @staticmethod
    def md5_code_return_only(string):
        result = MD5.new(data=string.encode('utf-8')).hexdigest()
        return result

    @staticmethod
    def vector_gen(string):
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

    def emg_question_crypto(self, encrypt, login, string):
        key = UserCrypto.md5_code_return_only(login).encode('utf-8')
        iv = UserCrypto.vector_gen(key.decode('utf-8'))
        cipher = AES.new(key, AES.MODE_CBC, iv)
        result = None
        try:
            if encrypt:
                string_enc = Padding.pad(string.encode('utf-8'), AES.block_size)
                result = base64.b64encode(cipher.encrypt(string_enc)).decode('utf-8')
            if not encrypt:
                string_enc = base64.b64decode(string.encode('utf-8'))
                result = Padding.unpad(cipher.decrypt(string_enc), AES.block_size).decode('utf-8')
            return result
        except SyntaxError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            self.Error_log.create_new_log("Crypto user: " + str(exc_obj) + " " + str(exc_tb.tb_lineno))
            return False


class MediaCrypto:
    Error_log = Reader.ReaderERROR()

    def __init__(self):
        print("init")

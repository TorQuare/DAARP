import random
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256, SHA512
import base64
import hashlib
import Reader

class User_crypto():

    def __init__(self):
        Error_log = Reader.Reader_ERROR()

    def Pass_crypto_mode_hash(self, string):
        S_512 = SHA512.new(data=string.encode('utf-8')).hexdigest()
        S_256 = SHA256.new(data=string.encode('utf-8')).hexdigest()
        result = S_512+S_256

        print (result)
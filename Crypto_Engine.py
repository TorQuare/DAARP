import random
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256, SHA512
from Crypto.Util import Padding
import base64
import Reader


class UserCrypto:
    Error_log = Reader.ReaderERROR()

    def __init__(self):
        print("init")

    def pass_crypto_mode_hash(self, string):
        result = None
        try:
            sha_512 = SHA512.new(data=string.encode('utf-8')).hexdigest()
            sha_256 = SHA256.new(data=string.encode('utf-8')).hexdigest()
            result = UserCrypto.md5_code_return_only(sha_256 + sha_512)
        except SyntaxError:
            self.Error_log.create_new_log("Crypto user")
        return result

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

    def aes_block_mode(self, encrypt, code, string):
        key = UserCrypto.md5_code_return_only(code).encode('utf-8')
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
            self.Error_log.create_new_log("Crypto user")
            return False    # wymyślić globalny problem w razie exception
        except ValueError:
            print("Inncorrect key aes_block_mode")
            return False

    @staticmethod
    def code_gen():
        code = []
        result = ""
        for i in range(5):
            if i == 0:
                value = random.randint(1, 9)
            else:
                value = random.randint(0, 9)
            code.append(value)
            if i >= 2:
                while code[i] == code[i-1] and code[i] == code[i-2]:
                    code[i] = random.randint(0, 9)
        for j in code:
            result += str(j)
        return result


class MediaCrypto(UserCrypto):

    def aes_stream_mode(self, encrypt, login_32, string):
        key = login_32.encode('utf-8')
        iv = UserCrypto.vector_gen(key.decode('utf-8'))
        cipher = AES.new(key, AES.MODE_CFB, iv)
        result = ""
        try:
            if encrypt:
                result = base64.b64encode(cipher.encrypt(string.encode('utf-8'))).decode('utf-8')
            if not encrypt:
                string_enc = base64.b64decode(string.encode('utf-8'))
                result = cipher.decrypt(string_enc).decode('utf-8')
        except SyntaxError:
            self.Error_log.create_new_log("Crypto user")
            return False    # wymyślić globalny problem w razie exception
        except ValueError:
            print("Inncorrect key aes_block_mode")
            return False
        return result

    @staticmethod
    def key_code_shaker(code):
        result = ""
        code_array = list(map(int, str(code)))
        print(code_array)
        pre_code = []
        key_code = []
        pre_code_iterator = 0
        flag = 0
        flag_ex = False
        while len(key_code) != 3:
            iterator = 0
            if flag:
                code_array[0] += 3
                if code_array[0] >= 10:
                    code_array[0] -= 8
            flag += 1
            if flag > 10:       # flaga blokująca niesończoną pętle
                flag_ex = True
                break
            for value in range(4):
                if value != 0 and value != 1:
                    if code_array[0] % value == 0:
                        for i in code_array:
                            if code_array[iterator] % value == 0:
                                pre_code.append(i)
                                pre_code_iterator += 1
                            iterator += 1
                        iterator = 0
                    elif code_array[0] % value == 1:
                        for i in code_array:
                            if code_array[iterator] % value == 1:
                                pre_code.append(i*2)
                                if pre_code[pre_code_iterator] >= 10:
                                    pre_code[pre_code_iterator] = pre_code[pre_code_iterator] - 9
                                pre_code_iterator += 1
                            iterator += 1
                        iterator = 0
            for i in reversed(pre_code):
                key_code.append(i)
            while len(key_code) > 3:
                if len(key_code) % 2 == 0 or len(key_code) % 3 == 0:
                    key_code.pop(1)
                else:
                    if key_code[2] % 2 == 0:
                        key_code.pop(4)
                        key_code.pop(0)
                    else:
                        key_code.pop(2)
            for i in key_code:
                if key_code[iterator] == 0:
                    key_code[iterator] = code_array[0]
                iterator += 1
        if flag_ex:
            return False
        for i in key_code:
            result += str(int(i))
        print(result)
        return result

    @staticmethod
    def login_code_gen(iteration, string):
        result = string
        for i in range(iteration):
            result = MediaCrypto.md5_code_return_only(result)
        return result

    def enc_string_generator(self, encrypt, code, login, string):
        key_code = list(map(int, str(MediaCrypto.key_code_shaker(code))))
        login_32 = []
        for i in key_code:
            login_32.append(MediaCrypto.login_code_gen(i, login))
        key_code.sort()
        step = [0, 2, 1]
        key_code[1] = int(key_code[1] / 2)
        key_code[0] = key_code[2] % 3
        if key_code[0] == 0:
            key_code[0] += 1
        if encrypt:
            step.sort()
        for j in step:
            if j == 0:
                for i in range(key_code[1]):  # AES_stream_mode
                    string = MediaCrypto.aes_stream_mode(self, encrypt, login_32[j], string)
            if j == 1:
                print(string, "  ", len(string))
                string = MediaCrypto.aes_block_mode(self, encrypt, login_32[j], string)
            if j == 2:
                for i in range(key_code[0]):
                    if len(string) < 200 or not encrypt:
                        try:
                            string = MediaCrypto.aes_stream_mode(self, encrypt, login_32[j], string)
                        except:
                            break
        print(string, "  ", len(string), "  ", key_code)
        return string

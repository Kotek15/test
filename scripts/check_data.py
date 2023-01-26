from scripts.table_manager import TableManager
from scripts.crypto import AESCipher
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES


class CheckData():
    def __init__(self, login_model: type):
        #self.worker_model = worker_model
        self.login_model = login_model
        key = b'Sixteen byte key'
        iv = b'Sixteen byte IV'
        iv = iv.ljust(16, b'\x00')
        self.cipher = AESCipher(key, iv)

    def check_user_exists(self, login: str, password: bytes):

        loginsList = self.login_model.objects.values_list('login', flat=True)
        list(loginsList)

        if login in loginsList:
            userData = self.login_model.objects.get(login=login)
            userCryptedPassword = userData.password
            userDecryptedPassword = self.cipher.decrypt(userCryptedPassword)
            if password == userDecryptedPassword:
                return 1
            else:
                return 0
        else:
            return 2

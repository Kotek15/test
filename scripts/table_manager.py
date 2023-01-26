from scripts.crypto import AESCipher

class TableManager:
    def __init__(self, login_model: type, worker_model: type):
        self.worker_model = worker_model
        self.login_model = login_model

    def add_worker(self, company: str,
                   firstname: str,
                   lastname: str):
        worker_data = self.worker_model()
        worker_data.save()

    def add_login(self, login: str, password: str):
        key = b'Sixteen byte key'
        iv = b'Sixteen byte IV'
        iv = iv.ljust(16, b'\x00')
        cipher = AESCipher(key, iv)
        passwordEncrypted = cipher.encrypt(password)
        login_data = self.login_model(login=login, password=passwordEncrypted)
        login_data.save()


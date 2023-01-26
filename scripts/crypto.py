from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self, key: bytes, iv: bytes):
        self.key = key
        self.iv = iv.ljust(16, b'\x00')

    def encrypt(self, data: str) -> bytes:
        data_bytes = data.encode()
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        padded_password = pad(data_bytes, AES.block_size, style='pkcs7')
        return cipher.encrypt(padded_password)

    def decrypt(self, data: bytes) -> str:
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        unpadded_password = unpad(cipher.decrypt(data), AES.block_size, style='pkcs7')
        return unpadded_password.decode()

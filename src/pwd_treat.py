from cryptography.fernet import Fernet

def get_key():
    file = open("key.txt", "r") 
    key = file.readline()
    return key

def crypt_password(password):
    password = password.encode()
    key = bytes(get_key().encode("utf-8"))
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(password)
    return ciphered_text
    
def decrypt_password(encrypted_pwd):
    key = bytes(get_key().encode("utf-8"))
    cipher_suite = Fernet(key)
    pwd_bytes = cipher_suite.decrypt(encrypted_pwd)
    pwd = bytes(pwd_bytes).decode("utf-8") #convert to string
    return pwd
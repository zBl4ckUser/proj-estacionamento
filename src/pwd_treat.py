from cryptography.fernet import Fernet

def new_key():
    key = Fernet.generate_key()
    file = open("key.txt", "wb")
    file.write(key)
    file.close()
    return key

def check_if_key_exist():
    import os.path
    if not os.path.isfile("key.txt"):
        new_key()

def get_key():
    file = open("key.txt", "r") 
    key = file.readline()
    file.close()
    return key

def crypt_password(password):
    password = password.encode()
    check_if_key_exist()
    key = bytes(get_key().encode("utf-8"))
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(password)
    return ciphered_text
    
def decrypt_password(encrypted_pwd):
    check_if_key_exist()
    key = bytes(get_key().encode("utf-8"))
    cipher_suite = Fernet(key)
    pwd_bytes = cipher_suite.decrypt(encrypted_pwd)
    pwd = bytes(pwd_bytes).decode("utf-8") #convert to string
    return pwd
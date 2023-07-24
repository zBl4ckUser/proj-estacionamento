from cryptography.fernet import Fernet

fernet_key = Fernet.generate_key()

arq = open("key.txt", "wb")
arq.write(fernet_key)
arq.close()
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
print(key)

plaintext = b"encryption is very useful"

ciphertext = f.encrypt(plaintext)
print(ciphertext)

decryptedtext = f.decrypt(ciphertext)
print(decryptedtext)
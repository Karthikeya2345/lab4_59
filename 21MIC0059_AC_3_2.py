from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

while True:
    try:
        key=DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass
def encrypt(msg):
    cipher=DES3.new(key,DES3.MODE_EAX)
    nonce=cipher.nonce
    ciphertext=cipher.encrypt(msg.encode('ascii'))
    return nonce,ciphertext

def decrypt(nonce,ciphertext):
    cipher=DES3.new(key,DES3.MODE_EAX,nonce=nonce)
    plaintext=cipher.decrypt(ciphertext)
    return plaintext.decode('ascii')

nonce,ciphertext=encrypt(input('Enter the message:'))
plaintext=decrypt(nonce,ciphertext)

print("Cipher text:", ciphertext)
print("Plain text:" ,plaintext)

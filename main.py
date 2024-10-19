from sys import maxsize as bound
from sympy import isprime

def create_public_key(p: int, q: int) -> tuple[int, int]:
    n = p * q
    e = __find_e(p)

    return e, n

def create_private_key(p: int, q: int) -> tuple[int, int]:
    n = p * q
    e = __find_e(p)
    phi = (p - 1) * (q - 1)

    # Find d such that (d * e) % phi = 1
    for k in range(1, bound):
        d = (1 + (k * phi)) / e
        if d.is_integer():
            return int(d), n

def __find_e(phi: int) -> int:
    for i in range(phi - 1, 1, -1):
        if isprime(i) and phi % i != 0:
            return i

def encrypt(public_key: tuple[int, int], plain_text : str, alpha: str) -> str:
    e, n = public_key
    cipher = []

    for ch in plain_text :
        index = alpha.index(ch) + 1
        encrypted_char = pow(index, e, n)
        cipher.append(str(encrypted_char))

    return ','.join(cipher)

def decrypt(private_key: tuple[int, int], cipher: str) -> str:
    d, n = private_key
    plain_text  = ''

    for num in cipher.split(','):
        plain_text  += chr(pow(int(num), d, n))

    return plain_text 

alpha = 'АБВГДЕЇЖЗИЙКЛМНОПРСТУФХЦЧШЩЄҐЬІЮЯ 0123456789'

plain_text  = 'ГОСТ24'
cipher = '310, 256, 385, 580, 218, 1, 256, 326'
p = 17
q = 41

public_key = create_public_key(p, q)
private_key = create_private_key(p, q)

encrypted_text = encrypt(public_key, plain_text , alpha)
decrypted_text = decrypt(private_key, cipher)

print(f'Plain text: {plain_text }')
print(f'Public key: {public_key}')
print(f'Cipher: {cipher}\n')

print(f'Encrypted text: {encrypted_text}')
print(f'Private key: {private_key}')
print(f'Decrypted text: {decrypted_text}')

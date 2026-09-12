import math
import random
import time
import matplotlib.pyplot as plt
# initialises variables for inputs
p = int(input("Enter an integer number"))
q = int(input("Enter another integer number"))

n = p * q
phi = (p - 1) * (q - 1)
tot = phi


# greatest common divisor -> think this is what's used to see if e is valid but idk
def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def is_valid_e(e, tot):
    return gcd(e, tot) == 1


e = int(input("Enter a value of e"))
# extended eulers algorithm

def eea(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = eea(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


g, x, y = eea(e, tot)
d = x % tot


# power mod function
def powerMod(a, b, n):
    if n == 1:
        return 0
    result = 1
    a = a % n
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        b = b // 2
        a = (a * a) % n
    return result

#naive_factoring_attack
def naive_attack(n):
    for i in range(2,math.isqrt(n) + 1):
        if n % i ==0:
            return i, n//i
    return "n is prime"


#primality test
def primality_check(n, k=20):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        d = d // 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = powerMod(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = powerMod(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def generate_bits(bits, k=20):
    while True:
        candidate = random.getrandbits(bits)
        candidate |= (1 << bits -1) | 1
        if primality_check(candidate, k ):
            return candidate


def main():
    bits = int(input("Enter bit-lengths for p and q"))
    p = generate_bits(bits)
    q = generate_bits(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = int(input("Enter a value of e: "))
    while not (is_valid_e(e, phi) and 1 < e < phi):
    n = p*q
    phi = (p-1) * (q-1)
    print(f"p = {p}, q = {q}, n = {n}")
    e = int(input("Enter a value of e: "))         
    while not (is_valid_e(e, phi) and 1 < e < phi): 
        e = int(input("Enter a value of e: "))
    print(f"The value of e chosen is {e}")
    g, x, y = eea(e, phi)
    d = x % phi
    mode = input("Enter E for encryption, D for decryption and N for the naive factoring attack")
    if mode.upper() == "E":
        message = int(input("Enter the message to be encrypted"))
        encrypted_message = powerMod(message,e,n)
        print(f"The encrypted message is {encrypted_message}")
    elif mode.upper() == "D":
        message = int(input("Enter the message to be decrypted"))
        decrypted_message = powerMod(message,d,n)
        print(f"The decrypted message is {decrypted_message}")
    elif mode.upper() == "N":
        p,q = naive_attack(n)
        phi = (p-1) * (q-1)
        g,x,y = eea(e,phi)
        d_recovered = x % phi
        print(f"The actual value of d is {d}")
        print(f"The value of d is {d_recovered}")


def rsa_setup(bits,k):
    p = generate_bits(bits,k)
    q = generate_bits(bits,k)
    n = p * q
    phi = (p-1) * (q-1)
    e = 3
    while is_valid_e(e,phi) == False:
        e +=2

    g,x,y = eea(e,phi)
    d = x % phi
    return n,e,d

def crack_rsa(n,e,cipher):
    recovered_p, recovered_q = naive_attack(n)
    recovered_phi = (recovered_p - 1) * (recovered_q - 1)
    g , x, y = eea(e, recovered_phi)
    recovered_d = x % recovered_phi
    message = powerMod(cipher, recovered_d,n)
    return message


def naive_factoring_attack(bit_sizes):
    results = []
    for bit in bit_sizes:
        n,e,d = rsa_setup(bit,20)
        message = 42
        cipher = powerMod(message,e,n)
        start_time = time.time()
        cracked_message = crack_rsa(n,e,cipher)
        end_time = time.time()

        time_taken = end_time - start_time
        success = bool(cracked_message == message)
        results.append((bit,n,time_taken,success))
        print(bit,n,time_taken,success)
    return results 




#main()
naive_factoring_attack([16, 24, 32])

import math
import random

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


# primality test
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
        e = int(input("Enter a value of e: "))
    print(f"The value of e chosen is {e}")
    g, x, y = eea(e, phi)
    d = x % phi
    mode = input("Enter E or D for the encrypt or decrypt ")
    if mode.upper() == "E":
        message = int(input("Enter the message to be encrypted"))
        encrypted_message = powerMod(message,e,n)
        print(f"The encrypted message is {encrypted_message}")
    if mode.upper() == "D":
        message = int(input("Enter the message to be decrypted"))
        decrypted_message = powerMod(message,d,n)
        print(f"The decrypted message is {decrypted_message}")


main()
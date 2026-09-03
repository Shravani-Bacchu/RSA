import math
import random

# initialises variables for inputs
p = int(input("Enter an integer number"))
q = int(input("Enter another integer number"))
<<<<<<< HEAD
e = int(input("Enter a value of e"))
n = p *q
phi = (p-1) * (q-1)
tot = phi
# function to find the greatest common divisor 
=======
n = p * q
phi = (p - 1) * (q - 1)
tot = phi


# greatest common divisor -> think this is what's used to see if e is valid but idk
>>>>>>> refs/rewritten/main
def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p
<<<<<<< HEAD
# function to check whether e is a valid exponent
def is_valid_e(e, tot):
    return gcd(e, tot) == 1

=======


def is_valid_e(e, tot):
    return gcd(e, tot) == 1


e = int(input("Enter a value of e"))
>>>>>>> refs/rewritten/main
if is_valid_e(e, tot) and (1 < e < tot):
    print("Yay, that works!")
else:
    while not (is_valid_e(e, tot) and (1 < e < tot)):
        e = int(input("Enter a value of e"))
    print(f"The value of e chosen is {e}")


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
    print(f"The value of d is {d}")
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


<<<<<<< HEAD
#primality test
def primality(n):
    for i in range(2,n-1):
        if n%i ==0:
            return False
    return True


=======
# primality-test function
def primality_test(n):
    if n < 2:
        return False
    elif n in (2, 3):
        return True
    elif n % 2 == 0:
        return False
    return None


def main():
    mode = input("Enter 'E' or 'D' for the encrypt function or the decrypt function")
    if mode =="E":
        message = int(input("Enter the message to be encrypted"))
        encrypted_msg = powerMod(message,e,n)
        print(encrypted_msg)
    elif mode == "D":
        encrypted_msg = int(input("Enter the message to be decrypted"))
        decrypted_function = powerMod(encrypted_msg,d,n)
        print(decrypted_function)
    else:
        print("Invalid Function!, try again")
>>>>>>> refs/rewritten/main

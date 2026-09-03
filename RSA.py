import math
# initialises variables for inputs
p = int(input("Enter an integer number"))
q = int(input("Enter another integer number"))
e = int(input("Enter a value of e"))
n = p *q
phi = (p-1) * (q-1)
tot = phi
# function to find the greatest common divisor 
def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p
# function to check whether e is a valid exponent
def is_valid_e(e, tot):
    return gcd(e, tot) == 1

if is_valid_e(e, tot) and (1 < e < tot):
    print("Yay, that works!")
else:
    while not (is_valid_e(e, tot) and (1 < e < tot)):
        e = int(input("Enter a value of e"))
    print(f"The value of e chosen is {e}")

#extended eulers algorithm 
def eea(a,b):
    if b==0:
        return (a,1,0)
    g,x1,y1 = eea(b, a%b)
    x = y1
    y = x1 - (a//b) * y1
    return g, x ,y 

g,x,y = eea(e,tot)
d = x % tot
print(f"The value of d is {d}")

#power mod function
def powerMod(a, b, n):
    if n == 1:
        return 0
    result = 1
    a = a % n
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        b = b //2
        a = (a*a) % n                 
    return result

print(f"The value of m is {powerMod(3,13,7)}")

#primality test
def primality(n):
    for i in range(2,n-1):
        if n%i ==0:
            return False
    return True



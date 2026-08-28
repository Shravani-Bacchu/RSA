import math
# initialises variables for inputs
p = int(input("Enter an integer number"))
q = int(input("Enter another integer number"))
n = p *q
phi = (p-1) * (q-1)
tot = phi
factors = []
# checks the factors of phi -> should be utilised later for checking if the value of e chosen is valid?
while  phi % 2 == 0:
    factors.append(2)
    phi //= 2
for i in range(3, int(math.sqrt(phi)) + 1, 2):
    while phi % i == 0:
        factors.append(i)
        phi //= i
if phi > 2:
    factors.append(phi)

print(factors)
# greatest common divisor -> think this is what's used to see if e is valid but idk 
def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p

def is_valid_e(e, tot):
    return gcd(e, tot) == 1

e = int(input("Enter a value of e"))
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


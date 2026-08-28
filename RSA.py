import math
# initialises variables for 
p = int(input("Enter an integer number"))
q = int(input("Enter another integer number"))
n = p *q
phi = (p-1) * (q-1)
tot = phi
factors = []

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

def eea(a,b):
    if b==0:
        return (a,1,0)
    g,x1,y1 = eea(b, a%b)
    x = y1
    y = x1 - (a//b) * y1
    return g, x ,y 

g,x,y = eea(e,tot)
d = x % tot
print(d)


message = int(input("Enter the message to encrypt "))
encrypted_msg = message**e % n
print(encrypted_msg)

decrypted_msg = encrypted_msg **d % n
print(decrypted_msg)
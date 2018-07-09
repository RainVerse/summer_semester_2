from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA256


message = 'Hello232asdasdadadsasdasdadasdad34234242342423'
m2='hell'
h = SHA256.new(message.encode('utf-8')).digest()
print(len(h))
h2= SHA256.new(m2.encode('utf-8')).digest()
key = DSA.generate(1024)
k = random.StrongRandom().randint(1, key.q-1)
sig = key.sign(h, k)
print(len(str(sig[0])),len(str(sig[1])))

print(len(str(key.y)))
print(len(str(key.g)))
print(len(str(key.p)))
print(len(str(key.q)))
print(len(str(key.x)))


y=int(str(key.y))
g=int(str(key.g))
p=int(str(key.p))
q=int(str(key.q))
x=int(str(key.x))

if DSA.construct((y,g,p,q,x)).verify(h, sig):
    print('OK')
else:
    print('Invalid Signature')

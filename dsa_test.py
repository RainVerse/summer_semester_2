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

print(len(str(key.__getattr__('y'))))
print(len(str(key.__getattr__('y'))))
print(len(str(key.__getattr__('y'))))
print(len(str(key.__getattr__('y'))))
print(len(str(key.__getattr__('y'))))


y=int(str(key.__getattr__('y')))
g=int(str(key.__getattr__('g')))
p=int(str(key.__getattr__('p')))
q=int(str(key.__getattr__('q')))
x=int(str(key.__getattr__('x')))

if DSA.construct((y,g,p,q,x)).verify(h, sig):
    print('OK')
else:
    print('Invalid Signature')

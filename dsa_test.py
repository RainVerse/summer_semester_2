from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA


message = 'Hello'
m2='hell'
h = SHA.new(message.encode('utf-8')).digest()
h2= SHA.new(m2.encode('utf-8')).digest()
key = DSA.generate(1024)
k = random.StrongRandom().randint(1, key.q-1)
sig = key.sign(h, k)
print(h)
print(k)
print(sig[0],sig[1])
if key.verify(h2, sig):
    print('OK')
else:
    print('Invalid Signature')
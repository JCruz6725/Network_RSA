from My_RSA import *
import json
import random
from math import gcd


print ('#' * 80)

print ('\n' , ' '*30, 'TESTING \n')

print ('#' * 80)
print ('\n\n')



''' 
#test (1)
print ('********************')

for i in range (0, 20):

    print (f'***** {i} ******')

    rsa = RSA(upper = 1024, lower = 0)
    string_t = 'hello'
    cypher = rsa.encrypt(string_t, rsa.get_keys())
    keys = rsa.get_keys()
    print (cypher)
    print (keys)
    
    print ('')
    pt = rsa.decrypt(cypher, rsa.get_keys())
    print (f'decrypt: "{pt}" ')
    
    
print ('********************')
'''

random.seed()

for _ in range(1):

    
    #print (f'q: {r.p}, p: {r.q}, n: {r.n} \n tot: {r.totient_var}  e: {r.e}, d: {r.d}')
    

    
    #text = "hello john"
    #print (text)
    try:
        print ('make obj')
        r = RSA()
        print (f'q: {r.p}, p: {r.q}, n: {r.n} \n tot: {r.totient_var}  e: {r.e}, d: {r.d}')
        #print (r.count)
        #cy = r.encrypt(text)
        #print(cy)
        #print(r.decrypt(cy))


    except Exception as e:
        pass
        #print (e)
    
    print ('\n\n')

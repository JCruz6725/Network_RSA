from My_RSA import *
import json




print ('********************')

for i in range (0, 20):

    print (f'***** {i} ******')

    rsa = RSA(upper = 1024, lower = 0)
    string_t = 'hello'
    cypher = rsa.encrypt(string_t, rsa.get_keys())
    print (cypher)
    print ('')
    pt = rsa.decrypt(cypher, rsa.get_keys())
    print (f'decrypt: "{pt}" ')
    
    
print ('********************')



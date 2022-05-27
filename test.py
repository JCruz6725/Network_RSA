from My_RSA import *
import json



print ('#' * 80)

print ('\n' , ' '*30, 'testing \n')

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




print (' ')

a = time.time()
r = RSA()

print (' ')
print(time.time() - a)

print()

print(f"{r.totient_var} \n \n ")

 
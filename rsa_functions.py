import random
from string_functions import *
#random.seed(20)

def random_int(lower_limit, upper_limit):
    r = random.randint(lower_limit, upper_limit)
    return r

def mod_exponentiation(char_val, key, tot_n):
    remainder = (char_val**key)%(tot_n)
    return remainder


def check_if_prime(n):
    if (n <= 1):
        return False
    else:
        for i in range(2, n):
            if (n % i == 0):
                return False
        return True


def get_primes_in_range (x, y):
    primes = []
    for i in range (x, y):
        if (check_if_prime(i)):
            primes.append(i)
    return primes

    
def get_p_and_q(lower_limit, upper_limit):
    """ return a tuple of p and q which are both prime numbers """
    primes = get_primes_in_range(lower_limit, upper_limit)

    while True:
        p = random_int(0, len(primes)-1)
        q = random_int(0, len(primes)-1)
        if (p != q):
            break
    
    return primes[p], primes [q]


def totient(p, q):
    t = (p-1)*(q-1)
    return t


def multi_mod_inverse(d, p , q):
    #1 = ( private * public ) % totient(p, q)

    for e in range(1, totient(p, q)):
        if ( ((d * e) % totient (p, q)) == 1):
            return e
    return -1

def is_relative_prime(a, b): ##### need to fix this and add it to the get keys function #####
    from math import gcd
    if (gcd(a,b) == 1):
        return True

    
def get_keys(lower, upper):
    
    upper_bound = upper
    lower_bound = lower
    private_key = -1

    while (private_key == -1):
        
        public_key = random_int(lower_bound, upper_bound)
        p , q = get_p_and_q(lower_bound, upper_bound)
        n = p*q
        tot_n = totient(p, q)
        private_key = multi_mod_inverse(public_key, p, q)


    keys = {'public_key': public_key,
            'private_key': private_key,
            'totient_n': tot_n,
            'n': n
            }

    return keys



def encrypt(plain_text, keys):
    public_key = keys['public_key']
    #tot_n = keys['totient_n']
    n = keys['n']


    plain_text_int = string_to_int_array(plain_text)
    cypher_text_int = []

    for i in plain_text_int:
    
        cypher_text_int.append (mod_exponentiation(i, public_key, n))

    return cypher_text_int




def decrypt(cypher_text_int_array, keys):

    private_key = keys['private_key']
    #tot_n = keys['totient_n']
    n = keys['n']

    plain_int_array = []

    #plain_text_int = string_to_int_array(plain_text)
    #cypher_text_int = []

    for i in cypher_text_int_array:
    
        plain_int_array.append(mod_exponentiation(i, private_key, n))

    return plain_int_array




    






'''


int_text = string_to_int_array('hello')

keys = get_keys()


print (is_relative_prime(keys['public_key'], keys['private_key']))


 
print (f"""public: {keys['public_key']}
private: {keys['private_key']}
tot_n : {keys['totient_n']} \n""")

cypher = encrypt('hello this plain txt', keys )
plain = decrypt(cypher, keys)



print (' ')
print (cypher)
print (' ')
print (plain)


print (int_array_to_srting(plain))

'''

import random
from string_functions import *
import json
random.seed(20)

class RSA():
    def __init__ (self, upper = 2**8, lower = 0):
        self.__lower = lower
        self.__upper = upper
        self.keys = self.get_keys(self.__lower, self.__upper)
        #self.__p
        #self.__q
        #self.__n
        #self.__tot
    
    
    def random_int(self, lower_limit, upper_limit):
        r = random.randint(lower_limit, upper_limit)
        return r

    def mod_exponentiation(self, char_val, key, tot_n):
        remainder = (char_val**key)%(tot_n)
        return remainder


    def check_if_prime(self, n):
        if (n <= 1):
            return False
        else:
            for i in range(2, n):
                if (n % i == 0):
                    return False
            return True


    def get_primes_in_range (self, x, y):
        primes = []
        for i in range (x, y):
            if (self.check_if_prime(i)):
                primes.append(i)
        return primes

        
    def get_p_and_q(self, lower_limit, upper_limit):
        """ return a tuple of p and q which are both prime numbers """
        primes = self.get_primes_in_range(lower_limit, upper_limit)

        while True:
            p = self.random_int(0, len(primes)-1)
            q = self.random_int(0, len(primes)-1)
            if (p != q):
                break
        
        return primes[p], primes [q]


    def totient(self, p, q):
        t = (p-1)*(q-1)
        return t


    def multi_mod_inverse(self, d, p , q):
        #1 = ( private * public ) % totient(p, q)

        for e in range(1, self.totient(p, q)):
            if ( ((d * e) % self.totient (p, q)) == 1):
                return e
        return -1


    def is_relative_prime(self, a, b): ##### need to fix this and add it to the get keys function #####
        from math import gcd
        if (gcd(a,b) == 1):
            return True

        
    def get_keys(self, lower, upper):
        
        upper_bound = upper
        lower_bound = lower
        private_key = -1

        while (private_key == -1):
            
            public_key = self.random_int(lower_bound, upper_bound)
            p , q = self.get_p_and_q(lower_bound, upper_bound)
            n = p*q
            tot_n = self.totient(p, q)
            private_key = self.multi_mod_inverse(public_key, p, q)


        keys = {'public_key': public_key,
                'private_key': private_key,
                'totient_n': tot_n,
                'n': n
                }

        return keys


    def encrypt(self, plain_text):
        public_key = self.keys['public_key']
        #tot_n = keys['totient_n']
        n = self.keys['n']

        plain_text_int = string_to_int_array(plain_text)
        cypher_text_int = []

        for i in plain_text_int:
            cypher_text_int.append(self.mod_exponentiation(i, public_key, n))

        cypher = {'data' : cypher_text_int}
        
        return cypher
        #return cypher_text_int
        

    def decrypt(self, cypher_text_json, keys):

        private_key = keys['private_key']
        #tot_n = keys['totient_n']
        n = keys['n']

        plain_int_array = []

        #plain_text_int = string_to_int_array(plain_text)
        #cypher_text_int = []

        for i in cypher_text_json['data']:
        
            plain_int_array.append(self.mod_exponentiation(i, private_key, n))

        return plain_int_array


    #################################
    # String manipulation functions #
    #################################


    def format_data_to_int_array(data):
        temp = ''
        int_array = []
        #print(s)
        for char in data:
            #print (char)
            if (char != ','):
                temp += char
            else:
              int_array.append(temp)
              temp = ''

        return int_array


    def to_int_array (string_array):
        num = [int(num, base=10) for num in string_array]
        return num


    def data_to_json(data):
        in_data = {'data':data}
        json_data = json.dumps(in_data)
        return json_data


    def string_to_int_array(string_text):
        int_array = []
        for char in string_text:   
            int_array.append(ord(char))

        return int_array


    def int_array_to_srting(self, int_array):
        string = ''
        for char in int_array:   
            string += (chr(char))

        return string

    






enc = RSA()
print (enc.keys)
string_t = 'hello'
cypher = enc.encrypt(string_t)
print (cypher)




print(enc.int_array_to_srting(enc.decrypt(cypher, enc.keys)))
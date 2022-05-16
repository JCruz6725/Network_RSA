import random
from string_functions import *
import json
import time
from math import gcd

#import Thread from threading
#random.seed(20)

class RSA():
    def __init__ (self):
    
        self.primes = self.sieve_for_primes_to(2**16)      
        self.p = self.get_big_prime()
        self.q = self.get_big_prime()        
        self.n = self.p * self.q
        self.totient_var = self.__totient(self.p, self.q)
     
        self.e = -1
        print ("getting E")
        
        while (self.e == -1 or self.e > self.totient_var or
                gcd(self.e, self.totient_var) != 1):
            self.e = self.get_big_prime()
         
        print (f"{gcd(self.e, self.totient_var)}"  )
        
     
     
     
    def get_big_prime(self, test_itteration = 500):
        number = -1
        while (number == -1):
            number = self.__random_odd_int(2**1023, 2**1024)
            #if (self.square_root_test(number)):
            if (self.miller_rabin_test(number, test_itteration)):
                prime = number
                return prime
            else:
                number = -1
                
    
    #################################

    def square_root_test(self, large_prime):
        
        for prime in self.primes:
            if (large_prime % prime == 0):
                return False
        return True

    ########################
    
    def miller_rabin_test(self, n, k):
        #Source ----> https://gist.github.com/Ayrx/5884790
        # Implementation uses the Miller-Rabin Primality Test
        # The optimal number of rounds for this test is 40
        # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
        # for justification

        # If number is even, it's a composite number

        if (n == 2):
            return True

        if (n % 2 == 0):
            return False

        r, s = 0, n - 1
        while (s % 2 == 0):
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, s, n)
            if (x == 1 or x == n - 1):
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if (x == n - 1):
                    break
            else:
                return False
        return True

    ########################
    
    
    
    def sieve_for_primes_to(self, n):
        #stack overflow.... 
        #https://stackoverflow.com/questions/16004407/a-fast-prime-number-sieve-in-python/18997575#18997575
        size = n//2
        sieve = [1]*size
        limit = int(n**0.5)
        for i in range(1,limit):
            if sieve[i]:
                val = 2*i+1
                tmp = ((size-1) - i)//val 
                sieve[i+val::val] = [0]*tmp
        return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]
    
    
        
    
    def __random_int(self, lower_limit, upper_limit):
        r = random.randint(lower_limit, upper_limit)
        return r
        
    def __random_odd_int(self, lower_limit, upper_limit):
        r_number = 2
        while (r_number%2 == 0):
            r_number = random.randint(lower_limit, upper_limit)
        return r_number    
        

    #################################################
    # math functions to get public and private keys #
    #################################################
    
    def __mod_exponentiation(self, char_val, key, tot_n):
        remainder = (char_val**key)%(tot_n)
        return remainder


    def __check_if_prime(self, n):
        #Remove this
        if (n <= 1):
            return False
        else:
            for i in range(2, n):
                if (n % i == 0):
                    return False
            return True


    def __get_primes_in_range (self, x, y):
        #Remove this
        primes = []
        for i in range (x, y):
            if (self.__check_if_prime(i)):
                primes.append(i)
        return primes
       

        

        
    def __get_p_and_q(self, lower_limit, upper_limit):
        """ return a tuple of p and q which are both prime numbers """
        primes = self.__get_primes_in_range(lower_limit, upper_limit)

        while True:
            p = self.__random_int(0, len(primes)-1)
            q = self.__random_int(0, len(primes)-1)
            if (p != q):
                break
        
        return primes[p], primes[q]


    def __totient(self, p, q):  
        t = (p-1)*(q-1)
        return t


    def __multi_mod_inverse(self, d, p , q):
        #'''1 = ( private * public ) % totient(p, q)'''
        tot = self.__totient(p, q)
       
        for e in range(1, tot):
            if ( ((d * e) % tot) == 1):
                return e
        return -1


    def __is_relative_prime(self, a, b): ##### need to fix this and add it to the get keys function #####
        from math import gcd
        if (gcd(a,b) == 1):
            return True
        
        
        
        
    ##########################
    # get/set keys functions #
    ##########################     
        
        
    def __set_keys(self, lower, upper):
        
        upper_bound = upper
        lower_bound = lower
        private_key = -1

        while (private_key == -1):
            
            public_key = self.__random_int(lower_bound, upper_bound)
            p , q = self.__get_p_and_q(lower_bound, upper_bound)
            n = p*q
            #tot_n = self.__totient(p, q)
            private_key = self.__multi_mod_inverse(public_key, p, q)
            
            if (self.__is_relative_prime(public_key, private_key) ==  False):
                print('not relative prime')
            


        keys = {'public_key': public_key,
                'private_key': private_key,
                #'totient_n': tot_n,
                'n': n,
                #'p': p,
                #'q':q, 
                }

        return keys


    def get_keys(self):
        return self.__keys


    #############################
    # encrypt/decrypt functions #
    #############################


    def encrypt(self, plain_text, keys):
        public_key = keys['private_key']
        n = keys['n']

        plain_text_int = string_to_int_array(plain_text)
        cypher_text_int = []

        for i in plain_text_int:
            cypher_text_int.append(self.__mod_exponentiation(i, public_key, n))

        cypher = {'data' : cypher_text_int}
        
        return cypher
        #return cypher_text_int
        

    def decrypt(self, cypher_text_json, keys):

        private_key = keys['public_key']
        n = keys['n']

        plain_int_array = []

        #plain_text_int = string_to_int_array(plain_text)
        #cypher_text_int = []

        for i in cypher_text_json['data']:        
            plain_int_array.append(self.__mod_exponentiation(i, private_key, n))

        #print(plain_int_array)

        plain_text_string = self.__int_array_to_srting(plain_int_array)
        return plain_text_string
        


    #################################
    # String manipulation functions #
    #################################
    def __int_array_to_srting(self, int_array):
        string = ''
        for char in int_array:   
            string += (chr(char))
        
        return string




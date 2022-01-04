# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 05:55:12 2021

@author: taway
"""

import socket
from my_hasher import md5_hasher
from rsa_functions import *
from string_functions import *
import json



keys = get_keys(upper = 256, lower = 0)
server_public_key = {'public_key':keys['public_key'], 'n':keys['n']}
server_private_key =  {'private_key':keys['private_key'], 'n':keys['n']}


data = str( server_public_key['public_key']  ) + ',' + str(server_public_key['n']) + ','
print (data)


HOST = '127.0.0.1'
PORT = 27000
user = 'john'
password = '123'

#for i in range (20):
#    password = md5_hasher(password)

print ('*** SERVER ***')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()

print('Connected by', addr)


conn.send(str(data).encode())




def server_chat_state():

    while True:

        data = conn.recv(1024).decode()
        print ('receive> ',data)
        if (data == 'quit'):
            break





def server_chat_state_rsa():

    while True:

        data = conn.recv(256).decode()
        data = json.loads(data)



        data = int_array_to_srting(decrypt(data['data'], keys))
        

        print ('receive> ',data)
        if (data == 'quit'):
            break









def server_log_state():
    while True:

        data_user = conn.recv(256).decode()
        data_pass = conn.recv(256).decode()

        if (data_user+data_pass == user+password):
            conn.send(b'1')
            break
        else:
            conn.send(b'0')

        print('Received >', data_user+data_pass)








def server_log_state_with_hash():
    while True:
        data_user = conn.recv(256).decode()
        data_pass = conn.recv(256).decode()
        data_pass = md5_hasher(data_pass)

        if (data_user+data_pass == user+password):
            conn.send(b'1')
            break
        else:
            conn.send(b'0')

        print('Received >', data_user+data_pass)






#server_log_state_with_hash()
server_chat_state_rsa()
conn.close()
print ('connection terminated')

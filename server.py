# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 05:55:12 2021

@author: taway
"""

import socket
from my_hasher import md5_hasher
from My_RSA import *
from string_functions import *
import json

rsa = RSA()
keys = rsa.get_keys(upper = 256, lower = 0)

server_public_key = {'public_key':keys['public_key'], 'n':keys['n']}
server_private_key =  {'private_key':keys['private_key'], 'n':keys['n']}

DATA_SIZE = 1024


# *************
# * Functions *
# *************


def server_chat_state(conn):

    while True:

        data = conn.recv(DATA_SIZE).decode()
        print ('receive> ',data)
        if (data == 'quit'):
            break


def server_chat_state_rsa(conn, keys):

    while True:
        data = conn.recv(DATA_SIZE).decode()
        data = json.loads(data)
        data = int_array_to_srting(decrypt(data['data'], keys))
        
        print ('receive> ',data)

        if (data == 'quit'):
            break


def server_log_state(conn):
    
    while True:
        data_user = conn.recv(DATA_SIZE).decode()
        data_pass = conn.recv(DATA_SIZE).decode()

        if (data_user+data_pass == user+password):
            conn.send(b'1')
            break
        else:
            conn.send(b'0')

        print('Received >', data_user+data_pass)


def server_log_state_with_hash(conn):

    while True:
        data_user = conn.recv(DATA_SIZE).decode()
        data_pass = conn.recv(DATA_SIZE).decode()
        data_pass = md5_hasher(data_pass)

        if (data_user+data_pass == user+password):
            conn.send(b'1')
            break
        else:
            conn.send(b'0')

        print('Received >', data_user+data_pass)


# ********
# * Main * 
# ******** 




print ('*** SERVER ***')

# Could add threading to server to continously listen for new connection. 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen()
conn, addr = s.accept()

print('Connected by', addr)
data = conn.recv(DATA_SIZE).decode()





#server_log_state_with_hash()
server_chat_state_rsa()
conn.close()
print ('connection terminated')
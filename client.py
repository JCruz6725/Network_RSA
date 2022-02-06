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
client_public_key = {'public_key':keys['public_key'], 'n':keys['n']}
client_private_key =  {'private_key':keys['private_key'], 'n':keys['n']}

HOST = '127.0.0.1'
PORT = 27000

#print ('*** CLIENT ***')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(client_public_key.encode())

#data = s.recv(256).decode()

#server_keys = to_int_array(format_data_to_int_array(data))
#server_keys = {'public_key':server_keys[0], 'n':server_keys[1]}


def client_chat_state():
    while True:
        data = str(input('send >'))
        s.send(data.encode())

        if (data == 'quit'):
            break


def client_chat_state_rsa():
    #keys = get_keys(upper = 256, lower = 0)
    
    while True:
        data = str(input('send >'))
        if (data == 'quit'):
            break

        cypher = {"data":encrypt(data, server_keys)}
        data = json.dumps(cypher)
        #print (data)
        s.send(data.encode())


def client_log_state():
    while True:
        data = str(input('send : username> '))
        s.send(data.encode())

        data = str(input('send : password> '))
        s.send(data.encode())

        if (s.recv(256).decode() == '1'):
            break


def client_log_state_with_hash():
    while True:
        data = str(input('send : username> '))
        s.send(data.encode())

        data = str(input('send : password> '))

        for i in range (19):
            data = md5_hasher(data)

        s.send(data.encode())

        if (s.recv(256).decode() == '1'):
            print ('log good')
            break


#client_log_state_with_hash()
client_chat_state_rsa()
s.close()
print ('connection terminated')

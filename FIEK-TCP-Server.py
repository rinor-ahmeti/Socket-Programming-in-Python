import numpy as np
import socket
import datetime
import threading
import pandas as pd 
import platform
from _thread import *
import re

def CheckEmail(email):

    regex = '^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.+-]'
    if re.search(regex,email):
        return f'Emaili juaj {email} eshte valid!'
    else:
        return f'Emaili juaj nuk eshte valid!'

def IPADDRESS():
    return f'IP Adresa e juaj eshte: {address[0]}'

def PORT():
    return f'PORTI I KLIENTIT ESHTE: {address[1]}'

def SERVERINFO():
    data = {'IPADDRESS': address[0], 'PORT': address[1], 'HOSTNAME': platform.node(), 'OS/VERSION': platform.platform()}  
    return f"\nIP Address: {address[0]}\nPORT: {address[1]}\nHOSTNAME: {platform.node()}\nOS: {platform.platform()}"
    

def COUNT(fjala):
    bashketingulloret = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
        'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'w', 'x', 'z']
    zanoret = ['a', 'e', 'i', 'o', 'u', 'y']
    cons = 0
    vow = 0
    request = str(fjala[1::]).lower()
    for i in range(0,len(request)):
        if request[i] in bashketingulloret:
            vow = vow+1
        elif request[i] in zanoret:
            cons = cons+1
    return f'Ne fjalen e dhene kemi {vow} bashketingullore dhe {cons} zanore'


def REVERSE(fjala): 
    #newWord = str(fjala[1:])
    #return ' '.join([word[::-1] for word in 
    #                 newWord.split(' ')])
   
    fjala2 = fjala[1::]
    for i in fjala2:
        word = fjala2[::-1] + ' '
    return word
  
    # fjala2 = str(fjala[1::]).split(" ")
    # output = ''
    # for i in fjala2:
    #     output = i[::-1] + ' '
    # return output.strip()


def PALINDROME(fjala):
    if fjala == reversed(fjala):
        return f'Eshte palindrom!'
    else:
        return f'Nuk eshte palindrom!'


def TIME():
    return datetime.datetime.now().strftime("%H:%M:%S %D")


def GAME():
    nums = np.random.randint(1, 35, 5)
    numrat = []
    for i in nums:
        numrat.append(i)
    return f'{numrat}'


def CONVERT(tipi, vlera2):
    vlera = float(vlera2)
    if tipi.upper().strip() == 'CMTOFEET':
        return vlera/30.48
    elif tipi.upper().strip() == 'FEETTOCM':
        return vlera*30.48
    elif tipi.upper().strip()== 'KMTOMILES':
        return vlera/1.609
    elif tipi.upper().strip()== 'MILETOKM':
        return vlera*1.609
    else:
        return f'Argumente jovalide!'

def GCF(a,b):
    a=float(a)
    b=float(b)
    i=1
    i = float(i)
    while i <=a and i <=b:
        if a%i == 0 and b % i == 0:
            factor = i
        i=i+1
    return (float)(factor)


def menu(kerkesa,connection): 
    try:
        request = kerkesa.split()
        serverResponse = ""
        if request[0].upper() == 'IPADDRESS':
            serverResponse = IPADDRESS()
        elif request[0].upper() == 'PORT':
            serverResponse = PORT()
        elif request[0].upper() == 'COUNT':
            serverResponse = COUNT(request) 
        elif request[0].upper() == 'REVERSE':
            serverResponse = REVERSE(request)
        elif request[0].upper() == 'PALINDROME':
            serverResponse = PALINDROME(request[1])
        elif request[0].upper() == 'TIME':
            serverResponse = TIME()
        elif request[0].upper() == 'GAME':
            serverResponse = GAME()
        elif request[0].upper() == 'CONVERT':
            serverResponse = CONVERT(request[1],request[2])
        elif request[0].upper() == 'GCF':
            serverResponse = GCF(request[1],request[2])
        elif request[0].upper() == 'SERVERINFO':
            serverResponse = SERVERINFO()
        elif request[0].upper() == 'CHECKEMAIL':
            serverResponse = CheckEmail(request[1])
        else: 
            serverResponse = 'Kerkesa juaj eshte invalide.'
        str(connection.sendall(str.encode(serverResponse)))
    except:
        serverResponse = 'Gabim ne server.'
        str(connection.sendall(str.encode(serverResponse)))
   
def multithread(connection):
    try:
        while True:
            data = connection.recv(128).decode()
            if not data:
                break
            menu(data, connection)
        connection.close()
    except:
        print("Ka ndodhur nje gabim.")


host = 'localhost'
port = 13000
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

print(f'Serveri jone eshte startuar ne portin: {port}')
server.listen(10)
print('Serveri po pret per ndonje kerkese!')

while True:
    (client,address)=server.accept()
    print(f'Lidhur ne serverin {address[0]} ne portin {address[1]}')
    start_new_thread(multithread, (client,))
server.close()
    
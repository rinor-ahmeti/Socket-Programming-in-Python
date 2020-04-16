import numpy as np
import socket
import datetime
import threading
import pandas as pd 
import platform
from _thread import *
import re

def ARMSTRONG(number):
   
    if not isDigit(number):
        return f'Ju lutem jepni nje numer!'
    shuma = 0
    number=(int)(number)
    temp = number
    while temp > 0:
        digit = temp % 10
        shuma = shuma + digit**3
        temp = temp//10

    if number == shuma:
        return f'{number} eshte numer i Armstrongut'
    else: 
        return f'{number} nuk eshte numer i Armstrongut'

def shuma(number):
    if not isDigit(number):
        return f'Ju lutem jepni nje numer!'
    if (int)(number)<0:
        return f'Ju lutem jepni nje numer pozitiv!'
    s=0
    number=(int)(number)
    for i in range(0,number+1):
        s=s+i 
    return f'Shuma e {number} numrave te pare duke perfshire edhe {number} eshte: {(str)(s)}'
   

def isDigit(number):
    try:
       int(number)
       return True
    except:
        return False
        raise ValueError("Jepni nje numer diskret!")

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
    return f"IP Address: {address[0]} PORT: {address[1]} HOSTNAME: {platform.node()} OS: {platform.platform()}"
    

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


def REVERSE(input):
    words = input
    output = ''
    for word in words:
        for c in reversed(word):
            output += c
        output += ' '    
    reverseword = output[0:8]
    return (str)(output.rstrip().replace(reverseword,''))


def PALINDROME(fjala):
    fjala2 = fjala[::-1]
    if fjala.upper()==fjala2.upper():
        return f'Eshte palindrom!'
    else:
        return f'Nuk eshte palindrom!'


def TIME():
    return datetime.datetime.now().strftime("%H:%M:%S %D")


def GAME():
    numz = np.random.choice(range(35),5,replace=False)
    numrat = []
    for i in numz:
        numrat.append(i)
    numrat.sort()    
    return f'{numrat}'


def CONVERT(tipi, vlera2):
    vlera = (float)(vlera2)
    if tipi.upper().strip() == 'CMTOFEET':
        return (str)(vlera/30.48)
    elif tipi.upper().strip() == 'FEETTOCM':
        return (str)(vlera*30.48)
    elif tipi.upper().strip()== 'KMTOMILES':
        return (str)(vlera/1.609)
    elif tipi.upper().strip()== 'MILETOKM':
        return (str)(vlera*1.609)
    else:
        return f'Argumente jovalide!'

def GCF(a,b):
    if not isDigit(a) and not isDigit(b):
        return f'Argumentet e funksionit duhet te jene numra te plote.'
        
    a=int(a)
    b=int(b)
    i=1
    i = int(i)
    while i <=a and i <=b:
        if a%i == 0 and b % i == 0:
            factor = i
        i=i+1
    return str((factor))
    
def menu(kerkesa,connection): 
    try:
        request = kerkesa.split(' ')
        serverResponse = ''
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
        elif request[0].upper() == 'SHUMA':
            serverResponse = shuma(request[1])
        elif request[0].upper() == 'ARMSTRONG':
            serverResponse = ARMSTRONG(request[1])
        else: 
            serverResponse = 'Kerkesa juaj eshte invalide per serverin tone.'
        str(connection.sendall(str.encode(serverResponse)))
    except:
        serverResponse = 'Gabim ne server.'
        (connection.sendall(str.encode(serverResponse)))
   
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
    
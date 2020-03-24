import numpy as np
import socket
import datetime
import threading
from _thread import *


def IPADDRESS():
    return f'IP Adresa e juaj eshte: {address[0]}'


def PORT():
    return f'PORTI I KLIENTIT ESHTE: {address[1]}'


def COUNT(fjala):
    bashketingulloret = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
        'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'w', 'x', 'z']
    zanoret = ['a', 'e', 'i', 'o', 'u', 'y']
    cons = 0
    vow = 0
    for i in fjala.lower():
        if i in bashketingulloret:
            vow = vow+1
        elif i in zanoret:
            cons = cons+1
    return f'Ne fjalen {fjala} kemi {vow} bashketingullore dhe {cons} zanore'


def REVERSE(fjala):
    fjala2 = ''
    for i in fjala:
        fjala2 = fjala2 + i
    fjala2 = fjala2[::-1]
    return fjala2


def PALINDROME(fjala):
    if fjala == REVERSE(fjala):
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


def CONVERT(tipi, vlera):
    if vlera < 0:
        print("Vlera e dhene eshte negative. Shkojme me vleren absolute")
        vlera = abs(vlera)
    if tipi.upper().strip() == 'CMTOFEET':
        vlera = vlera/float(30.48)
        return f'{vlera} ft'
    elif tipi.upper().strip() == 'FEETTOCM':
        vlera = vlera*float(30.48)
        return f'{vlera} cm'
    elif tipi.upper().strip()== 'KMTOMILES':
        vlera = vlera/float(1.609)
        return f'{vlera} miles'
    elif tipi.upper().strip()== 'MILETOKM':
        vlera = vlera*float(1.609)
        return f'{vlera} km' 
    else:
        return f'Argumente jovalide!'


def menu(kerkesa,connection): ## REVERSE ADI 0 edhe antari. 0 REVESR, ANTARI ADI
    try:
        request = kerkesa.split()
        serverResponse = ""
        if request[0] == 'IPADDRESS':
            serverResponse = IPADDRESS()
        elif request[0] == 'PORT':
            serverResponse = PORT()
        elif request[0] == 'COUNT':
            serverResponse = COUNT(request[1]) 
        elif request[0] == 'REVERSE':
            serverResponse = REVERSE(request[1])
        elif request[0] == 'PALINDROME':
            serverResponse = PALINDROME(request[1])
        elif request[0] == 'TIME':
            serverResponse = TIME()
        elif request[0] == 'GAME':
            serverResponse = GAME()
        elif request[0] == 'CONVERT':
            serverResponse = CONVERT(request[1],request[2])
        else: 
            serverResponse = 'Kerkesa juaj per serverin eshte invalide.'
        connection.sendall(str.encode(serverResponse))
    except:
        serverResponse = 'Gabim ne server.'
        connection.sendall(str.encode(serverResponse))
   
def multithread(connection):
    while True:
        data = connection.recv(128).decode()
        if not data:
            break
        menu(data, connection)
    connection.close()
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
    
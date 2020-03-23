import numpy as np
import socket 
import datetime

def IPADDRESS():
    return f'IP Adresa e juaj eshte: {address[0]}'

def PORT():
    return f'PORTI I KLIENTIT ESHTE: {address[1]}'

def COUNT(fjala):
    bashketingulloret = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','w','x','z']
    zanoret=['a','e','i','o','u','y']
    cons=0
    vow=0
    for i in fjala.lower():
        if i in bashketingulloret:
            vow=vow+1
        elif i in zanoret: 
            cons=cons+1   
    return f'Ne fjalen {fjala} kemi {vow} bashketingullore dhe {cons} zanore'

def REVERSE(fjala): 
    fjala2 = ''
    for i in fjala:
        fjala2 = fjala2 + i
    fjala2 = fjala2[::-1]
    return fjala2

def PALINDROME(fjala):
    if fjala==REVERSE(fjala):
        return True 
    else:
        return False

def TIME():
    return datetime.datetime.now().strftime("%H:%M:%S %D")

def GAME():
    nums = np.random.randint(1,35,5)
    numrat = []
    for i in nums:
        numrat.append(i)
    return numrat

def CONVERT(tipi,vlera):
    if vlera<0:
        print("Vlera e dhene eshte negative. Shkojme me vleren absolute")
        vlera=abs(vlera)
    if tipi=='cmToFeet':
        vlera=vlera/float(30.48) 
        return str(vlera) + ' ft'
    elif tipi =='FeetToCm':
        vlera=vlera*float(30.48) 
        return str(vlera) + ' cm'
    elif tipi=='kmToMiles':
        vlera=vlera/float(1.609)
        return str(vlera) + ' miles'
    elif tipi=='MileToKm':
        vlera=vlera*float(1.609) 
        return str(vlera) + ' km'
    else:
        print('Argumente jovalide!')

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
    kerkesa = client.recv(1024) 
    print(f'Kerkesa nga klienti: {kerkesa.decode("utf-8")}')
    kerkesaMadhe = kerkesa.lower()
    print(f'PERGJIGJA E SERVERIT: {kerkesaMadhe.decode("utf-8")}')
    client.send(kerkesaMadhe)
    client.close()
    print("U mbyll sesioni")

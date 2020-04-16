import socket
import re
import keyboard 

def isDigit(number):
    try:
       int(number)
       return True
    except:
        raise ValueError("Jepni nje numer diskret!")
        

serverName = input("Shenoni adresen e serverit apo leni zbrazet per default:")
serverPort = input("Shenoni portin e serverit apo leni zbrazet per default:")
if serverName=='' or serverName=='localhost':
    serverName='localhost'
else:
    raise('Ju lutem qendroni ne localhost!')
if serverPort == '' or int(serverPort) == 13000:
    serverPort = 13000
else:
    raise('Ju lutem jepni portin e sakte.')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
pair = (serverName,serverPort)


while True:
    try:
        kerkesa = input("Shenoni JO per ta ndalur programin.\nShenoni kerkesen per serverin:")
        
        if kerkesa.upper()=='JO':
            print("Keni dalur me sukses nga serveri.")
            break
        elif (len(kerkesa.encode()) > 128):
            print("Kerkesa juaj eshte me e madhe se 128 bytes(1024 bits).")
            continue
        elif (kerkesa.strip() == ""):
            print("Serveri jone pranon edhe kerkesa boshe :)")
            continue
        s.sendto(str.encode(kerkesa),pair)
        data = s.recvfrom(128) 
        print("Pergjigja e serverit: " + repr(data[0].decode()))
    except:
        print("Gabim ne server. Provoni perseri!")
    

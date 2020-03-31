import socket

serverName = input("Shenoni adresen e serverit apo leni zbrazet per default:")
serverPort = ''
try:
    serverPort = (int)(input("Shkruajeni numrin e portit apo leni zbrazet per default:"))
except:
    raise Exception("Gabim! Porti i dhene duhet te jete diskret!")
if serverName=='':
    serverName='localhost'

if serverPort == '':
    serverPort = 13000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pair = (serverName,serverPort)
s.connect(pair)


while True:
    try:
        kerkesa = input("Shenoni JO per ta ndalur programin.\nShenoni kerkesen per serverin:")
        if kerkesa.upper()=='JO':
            print("Keni dalur me sukses nga serveri.")
            break
        elif (len(kerkesa.encode()) > 128):
            print("Kerkesa juaj eshte me e madhe se 128 bytes(1024 bits).")
            continue
        elif (kerkesa == ""):
            continue
        s.sendto(str.encode(kerkesa),pair)
        data = s.recvfrom(128)
        print("Pergjigja e serverit: " + str(data[0].decode("utf-8")))
    except:
        print("Gabim ne server. Provoni perseri!")
    


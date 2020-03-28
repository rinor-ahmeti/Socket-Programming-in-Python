import socket

serverName = 'localhost'
serverPort = 13000

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
        elif (kerkesa == ""):
            continue
        s.sendto(str.encode(kerkesa),pair)
        data = s.recvfrom(128) 
        print("Pergjigja e serverit: " + repr(data[0].decode()))
    except:
        print("Gabim ne server. Provoni perseri!")
    

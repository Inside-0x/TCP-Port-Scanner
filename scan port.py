import socket 
import sys 
if len(sys.argv) != 2:
    print("Usage: ./1.py <ip> ")
    sys.exit(0)
host = sys.argv[1]
l=int(input)
i=int(input)
p=range(l,i)    




port = sys.argv[2]
host =str(input())
soc =socket.socket()
#note  SOCK_STREAM TCP | SOCK_DGRAM UDP
print(f"[* Host-name ] : {host} ")


for ports in port :
    try :
        soc.connect((host,port))
        print(port,socket.getservbyport(port))
    except :
        pass
soc.close()
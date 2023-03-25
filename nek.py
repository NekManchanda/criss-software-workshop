import socket

serverIP = '172.17.29.11'
serverPORT = 6000

serveraddress = (serverIP, serverPORT)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

message = "hi, i am nek manchanda, my ID is 2021A7PS0576P"

bytestosend = str.encode(message)

UDPClientSocket.sendto(bytestosend,serveraddress)

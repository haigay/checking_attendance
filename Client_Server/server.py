import socket
import os

bufferSize = 1024
svPort = 2222
svIp = '169.254.50.187'

RPIsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIsocket.bind((svIp, svPort))
print("Server đang chạy....")

def send_file(file_path, address):
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(bufferSize)
            if not data:
                break
            RPIsocket.sendto(data, address)
        print('Gửi thành công')

while True:
    message, address = RPIsocket.recvfrom(bufferSize)
    message = message.decode('utf-8')

    print (message)

    print('Address client: ', address[0])

    

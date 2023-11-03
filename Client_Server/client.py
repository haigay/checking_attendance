import socket

serverAddress = ('169.254.50.187', 2222)
bufferSize = 1024

UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    request = input("Gui: ")
    request = request.encode('utf-8')

    UDPClient.sendto(request, serverAddress)

    if request == b'Gui':
        # Nếu client gửi lệnh "Gui," thì bạn cần nhận và lưu trữ file "trainer.yml" từ server.
        with open('trainer.yml', 'wb') as file:
            while True:
                data, address = UDPClient.recvfrom(bufferSize)
                if data == b'File not found':
                    print('File not found on the server.')
                    break
                file.write(data)
                if len(data) < bufferSize:
                    print("Nhan thanh cong")
                    break


        print('Ip address: ', address[0])
        print('Port: ', address[1])

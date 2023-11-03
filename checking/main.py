import socket
import tmp
# Thông tin kết nối socket
host = '169.254.50.187'
port = 8000
chunk_size = 4096

# Tạo socket và lắng nghe kết nối từ client
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print('Đang chờ kết nối từ client...')

# Chấp nhận kết nối từ client
client_socket, address = server_socket.accept()
print('Đã kết nối tới:', address)

# Vòng lặp để nhận message từ client
while True:
    # Nhận dữ liệu từ client
    data = client_socket.recv(chunk_size)

    # Giải mã dữ liệu nhận được
    message = data.decode()

    # In ra message từ client và cập nhật sang file excel
    tmp.update_xlsx(path=r'data.xlsx', id = message)
    print('Received message:', message)

    # Nếu message là 'q', thoát khỏi vòng lặp
    if message == 'q':
        break

# Đóng kết nối socket
client_socket.close()
server_socket.close()
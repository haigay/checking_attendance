from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import os
import zipfile
import shutil

# Tạo thư mục để lưu hình ảnh
face_id = input("\n Nhập mssv: ")
folder = f'datasets/{face_id}'
if not os.path.exists(folder):
    os.makedirs(folder)

# Khởi tạo PiCamera
camera = PiCamera()
camera.resolution = (480, 320)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(480, 320))

# Load file cascade
face_cascade = cv2.CascadeClassifier('/home/admin/Desktop/Face_recognition/haarcascade_frontalface_default.xml')

print("\n Nhìn vào camera chờ chụp hình...")
count = 0

# Chụp hình
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image = cv2.flip(image, -1)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Frame", image)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == 32:
        img_path = f'{folder}/Image {count}.jpg'
        cv2.imwrite(img_path, gray[y:y+h, x:x+w])
        count += 1
    if count > 50:
        print("\n Đã chụp hình xong...")
        break 
        
    rawCapture.truncate(0)
cv2.destroyAllWindows()



# Nén thư mục
"""zip_file_path = f'datasets.zip'
with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for foldername, subfolders, filenames in os.walk(f'datasets/'):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            arcname = os.path.relpath(filepath,f'datasets/')
            zipf.write(filepath, arcname=arcname)
shutil.rmtree(folder)

# Gửi file zip qua cho server
import socket
server_ip = '169.254.50.187'
server_port = 8000

# Tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Gửi file
with open(zip_file_path, 'rb') as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client_socket.send(data)
# Xóa tệp sau khi gửi thành công
os.remove(zip_file_path)

print('\n Đã gửi dữ liệu qua cho server.')
client_socket.close()"""






from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import os
import subprocess
import time
import socket
import LCD_i2c

LCD_i2c.init(0x27, 1)
LCD_i2c.write(1,0,"Cho diem danh")
# Khởi tạo camera
camera = PiCamera()
camera.resolution = (368, 288)
camera.framerate = 20
rawCapture = PiRGBArray(camera, size=(368, 288))

#Khoi tao socket
serverAddress = ('192.168.137.1', 2222)
bufferSize = 1024

UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Local Binary Patterns Histograms
recognizer = cv2.face.LBPHFaceRecognizer_create()

#Load file train
recognizer.read('/home/admin/Desktop/Face_recognition/Trainer.yml')

#Load file cascade
face_cascade = cv2.CascadeClassifier('/home/admin/Desktop/Face_recognition/haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image = cv2.flip(image,-1)
    
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (100, 100), flags = cv2.CASCADE_SCALE_IMAGE)
    
    # Nhận diện
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        #cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        id = str(id)
        folder = f'Newdataset/{id}'
        if not os.path.exists(folder):
            os.makedirs(folder)

        if (40< confidence < 60):     
            confidence = "{0}%".format(round(confidence))
            count = len(os.listdir(f'Newdataset/{id}'))
            img_path = f'{folder}/Image{count}.jpg'
            cv2.imwrite(img_path, roi_gray)
            print(id, confidence)
            LCD_i2c.clear()
            LCD_i2c.write(4,0,id)
            
            # Gửi message đến server
            #request = id.encode('utf-8')
            #UDPClient.sendto(request, serverAddress)
            
            #Restart
            rawCapture.truncate(0)
            
            time.sleep(0.5)
            subprocess.call(['python','/home/admin/Desktop/Face_recognition/test_model.py'])
        else:
            id = "unknown"
            confidence = "0%"        
            print(id, confidence)
    
  
        
    if cv2.waitKey(1) & 0xff == ord("q"):
        exit()
    rawCapture.truncate(0)
    
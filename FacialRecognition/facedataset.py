import cv2
import os
import sys

# Disesuakian dengan ukuran screen Ex. 1280 x 720
cam = cv2.VideoCapture(0)
cam.set(3, 640) # Lebar Kamera
cam.set(4, 480) # Tinggi Kamera



face_detector = cv2.CascadeClassifier('Your Path\haarcascade_frontalface_default.xml')

# id untuk setiap potret
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, +1) # flip video image Horizontal Kalau Diganti -1 Vertical
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Menyimpan Data Hasil Foto
        cv2.imwrite("Path Disesuakian dengan Device" + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")

cam.release()
cv2.destroyAllWindows()



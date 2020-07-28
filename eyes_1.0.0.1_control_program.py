import cv2, time

import pyautogui

from time import time

first_frame = None
_author__ = 'The control software has been written Jurijus Pacalovas.'

print(_author__)

print("Program that control computer (control program). By this program you can control computer by eyes. I enjoy writing programs.")
namez = input("Please, enter for move mouse 1, 2, 3, 4, 5, 6, 7 ")
w1=0
q1=0

rt1=0
rt2=0
rt3=0
rt4=0

qmoveanywhere1=0
if namez=="6":
    w1=0
    
qmoveanywhere1=0
if namez=="1":
    w1=100
    

if namez=="2":
    w1=200
    

if namez=="3":
    w2=300
    

if namez=="4":
    w1=400
    

if namez=="5":
    w1=500

if namez=="7":
    qmoveanywhere1=1


video = cv2.VideoCapture(0)

    
x=0
x1=0
x2=0
x = time()

while True:
    check, frame = video.read()
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0) 

    if first_frame is None:
        first_frame = gray 

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2) 

    cnts = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    for contour in cnts:
        if cv2.contourArea(contour) < 1000: 
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        

        if qmoveanywhere1==1 and x>=200 and x<=255 or qmoveanywhere1==1 and y>=200 and y<=255:
            w1=200

        if qmoveanywhere1==1 and x>=400 and x<=455 or qmoveanywhere1==1 and y>=400 and x<=455:
            w1=400

        if qmoveanywhere1==1 and x>=500 and x<=555 or qmoveanywhere1==1 and y>=500 and x<=555:
            w1=500

        if qmoveanywhere1==1 and x>=0 and x<=50 or qmoveanywhere1==1 and x>=0 and y<=50:
            w1=0

        if qmoveanywhere1==1 and x>=256 and x<=305 or qmoveanywhere1==1  and y>=300 and y<=355:
            w1=200

        if qmoveanywhere1==1 and x<=400 and x>=355 or qmoveanywhere1==1 and y>=400 and y<=455:
            w1=500
        
            
        w=x+w1
        h=y+w1
       
        
        if x>=1:
            rt1=x
            rt2=y

        if x>=2:
            rt3=x
            rt4=y
            
            pyautogui.click(w, h)
            
            x=0
            x1=0
            x2=0
            x = time()
              
        
        pyautogui.moveTo(w, h, duration = 1) 
        
    

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    print(gray)
    print(delta_frame)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows

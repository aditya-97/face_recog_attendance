import os
import sqlite3
from Tkinter import *
import cv2
import numpy as np
import tkMessageBox


def log(uname,uroll):
    conn = sqlite3.connect('users.db')
    if not os.path.exists('./dataset'):
        os.makedirs('./dataset')
    c = conn.cursor()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')      
  #uname,uroll = sub1()
    uroll = int(uroll)
    cap = cv2.VideoCapture(0)
  #uname = input("Enter your name: ")
  #uroll = input("Enter your roll no: ")
  #if not os.path.exists('./dataset/'+str(uname)):
  #  os.makedirs('./dataset/'+str(uname))
    c.execute('INSERT INTO lecture1 (Name,Roll_No) VALUES (?,?)', (uname,uroll))
  #uid = c.lastrowid
    sampleNum = 0
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 7)
        for (x,y,w,h) in faces:
            sampleNum = sampleNum+1
            cv2.imwrite("dataset/User."+str(uroll)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.waitKey(100)
        cv2.imshow('img',img)
        cv2.waitKey(1);
        if sampleNum > 40:
            break
    cap.release()
    conn.commit()
    conn.close()
    cv2.destroyAllWindows()
import cv2
import numpy as np 
import sqlite3
import os
import time
#print (cv2.__version__)
def get_user():
  conn = sqlite3.connect('users.db')
  c = conn.cursor()
  fname = "recognizer/trainingData.yml"
  if not os.path.isfile(fname):
    print("Please train the data first")
    exit(0)
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  cap = cv2.VideoCapture(0)
  recognizer = cv2.face.LBPHFaceRecognizer_create()
  recognizer.read(fname)
  i=0
  j=0
  detect=''
  while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 7)
    for (x,y,w,h) in faces:
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
      ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
      c.execute("select Name from Lecture1 where Roll_No = (?);", (ids,))
      result = c.fetchall()
      #print result[0][0]
    #print ids
    #print conf
      print "i= %d"%i
      print "j= %d"%j
      name = result[0][0]
      if conf < 50:
        i=i+1
        cv2.putText(img, name, (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
      else:
        cv2.putText(img, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
        j=j+1
    cv2.imshow('Face Recognizer',img)
    k = cv2.waitKey(30) & 0xff
    time.sleep(0.01)
    if k == 27:
      break
    if i>30:
      i=0
      detect=name
      break
    if j>30:
      detect='No Match'
      j=0
      break
  cap.release()
  cv2.destroyAllWindows()
  return detect

#!/usr/bin/env python3
import cv2
import rospy
import numpy as np
from std_msgs.msg import String

rospy.init_node('face_control',anonymous=True)
rospy.loginfo('Face detection was started')
def talker (check):
	pub = rospy.Publisher('face_control',String, queue_size=15)
	if check == 0:
		answer = "It's our employee!"
	else:
		answer = "Unknown!"
	#answer = "Unknown!"
	rate = rospy.Rate(0.00001)
	rospy.loginfo(answer)
	pub.publish(answer)
	#time.sleep(5)





recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

# ID counter
id = 0

# Names related to IDs
names = ['None','Andrey', 'Katya', 'Nikto', 'Z', 'W'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

print(cam.get(3))
print(cam.get(4))

#if (os.path.isfile("Python/Unknown.jpeg")==True):
#    os.remove("Python/Unknown.jpeg")

sent=False
id_check1=0
id_check2=0
ts = False

while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    check=0
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 12, minSize = (int(minW), int(minH)))
    lower_color = np.array([49, 100, 0])
    upper_color = np.array([120, 255, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    
    for(x,y,w,h) in faces:
        
        #time.sleep(3)
        
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w,y+h), (60, 20, 220), 2)
        cv2.imwrite("Python/Unknown.jpeg", img)
        
        
        #id_check1=id
        #print(id)
        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 70):
            
            #if (id_check2!=id_check1):
            check+=1
            
            
            
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            
        else:
            id = "Unknown"
            #confidence = "  {0}%".format(round(100 - confidence))
            confidence = "  {0}%".format(0)
            #now = datetime.datetime.now()
            cv2.imwrite("Python/Unknown.jpeg", img)
        
        if (id == "Unknown"):
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            #cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
            
        else:
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
            cv2.rectangle(img, (x,y), (x+w,y+h), (154,255,0), 2)
            
            
        #print(faces)
        cropped = mask[x:x+w,y+h:y+2*h]
        #cv2.imshow('Cropped',cropped)
        m=(len(cropped))
        n=(len(cropped[0]))
        #print('размер фрагмента (в пикселях): ',n,'*',m,'=',n*m)
        #print('из них:')
        color=0
        notcolor=0
        cv2.imshow('Video',img) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#print(len(faces))
    if id == "Unknown":
    	check = 1
    else:
    	check = 0
    talker(check)	
cam.release()
cv2.destroyAllWindows()

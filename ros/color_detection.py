#!/usr/bin/env python3
import cv2
import numpy as np
import rospy
import time
from std_msgs.msg import String
rospy.init_node('color_control',anonymous=True)
rospy.loginfo('Color detection was started')
def talker ():
	pub = rospy.Publisher('Uniform',String, queue_size=15)
	answer = "Alright! It is an employee"
	rate = rospy.Rate(0.00001)
	rospy.loginfo(answer)
	pub.publish(answer)
	
def live_video(camera_port=0):
        
        video_capture = cv2.VideoCapture(camera_port)
        color_yellow = (0,255,255)
        

        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            # Display the resulting frame
            cv2.imshow('Video', frame)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            low_green = np.array((65,107,2),np.uint8)
            high_green = np.array((95,255,255),np.uint8)
            #mask1 = cv2.inRange(hsv,(0,50,20),(5,255,255))
            #mask2 = cv2.inRange(hsv,(175,50,20),(180,255,255)) 
            mask = cv2.inRange(hsv, low_green, high_green)
            #mask = cv2.bitwise_or(mask1,mask2)
            #cv2.imshow('mask',mask)
            #new part
            moments = cv2.moments(mask,1)
            sum_y = moments ['m01']
            sum_x = moments ['m10']
            sum_pixel = moments['m00']
            		
            if sum_pixel > 1500:
            	talker()
            	x = int(sum_x/sum_pixel)
            	y = int(sum_y/sum_pixel)
            	cv2.circle(frame, (x,y), 10, (0,0,255), -1)
            	cv2.putText(frame, "%d-%d" % (x,y), (x+50, y-50), cv2.FONT_HERSHEY_SIMPLEX,1,color_yellow,2)
            	
            #cv2.imshow('mask',mask)
            #cv2.imshow('final',frame)







            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        
	#video_capture.release()
	#cv2.destroyAllWindows() 
live_video()

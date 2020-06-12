#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import String
'''
def face(data):
	if data.data >= 'Unknown!':
		rospy.loginfo('Alarm! Unknown is inside the room',String,data.data)
def uniform(data):
	if data.data < 'Alright! It is an employee':
		rospy.loginfo('Alarm! Employee is without uniform',String,data.data)
def listener():def callback(data):
    rospy.loginfo(rospy.get_name()+"I heard %s",data.data)

def listener():def callback(data):
    rospy.loginfo(rospy.get_name()+"I heard %s",data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
	rospy.init_node('Email',anonymous=True)
	rospy.Subscriber('face_control', String, face)
	rospy.Subscriber('Uniform', String, uniform)
	rospy.spin()
if __name__ == '__main__':
    listener()'''
    
def callback(data):
	if data.data>='Unknown!':
    		rospy.loginfo('Sending security email...')

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("face_control", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

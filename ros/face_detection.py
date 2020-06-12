#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import String
rospy.init_node('face_control',anonymous=True)
rospy.loginfo('Face detection was started')
def talker ():
	pub = rospy.Publisher('face_control',String, queue_size=15)
	answer = "Unknown!"
	rate = rospy.Rate(0.00001)
	rospy.loginfo(answer)
	pub.publish(answer)
	time.sleep(5)
while True:
	talker()

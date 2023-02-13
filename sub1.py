#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def this_course(data: str):
	rospy.loginfo("I am also learning %s", data.data)
	
def listener():
	rospy.init_node("sub_anothernode",anonymous=True)
	rospy.Subscriber('first_lecture',String, this_course)
	rospy.spin()

if __name__ == '__main__':
	listener()

#!/usr/bin/env python3

# creates a ros node that controls two servo motors
# on a arduino running ros serial 
# this node accepts JointState which is
# --------------- 
# would the datastructure look like
# jointStateObj.name = ["neck_yaw", "neck_pitch"]
# jointStateObj.position = [180,0]
# jointStateObj.velocity# unused
# jointStateObj.effort#unused
# ---------------
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20210307



import rospy
import math

from std_msgs.msg import UInt16
from sensor_msgs.msg import JointState


global yaw_servo
global sub
global yaw_servo_position
yaw_servo_position = UInt16()

def move_servos(msg):
    servo_yaw =int(msg.position[0])
    print(msg)
    print(servo_yaw)
    inteager_yaw_angle = 0
    yaw_servo_position.data = int(msg.position[0])
    # send an int angle to move the servo position to 0-180  
    yaw_servo.publish(yaw_servo_position)

if __name__ == "__main__":
    rospy.init_node("head_mover")
    yaw_servo = rospy.Publisher("servo1",UInt16, queue_size=1)

    sub=rospy.Subscriber("move_head",JointState,move_servos)
    rate=rospy.Rate(10)
    print("servo_mover: Running")
    while not rospy.is_shutdown():
        rate.sleep()
    
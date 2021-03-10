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
global pitch_servo
global sub
global yaw_servo_position
global pitch_servo_position

# setting up interger variables 
#     the arduino only accepts integers
yaw_servo_position = UInt16()
pitch_servo_position = UInt16()

def move_servos(msg):
    print(msg)

    print(msg.position[0])
    print(msg.position[1])
    
    # convert float angle radians -pi/2 to pi/2 to integer degrees 0-180 
    yaw_servo_position.data   = int(msg.position[0])
    pitch_servo_position.data = int(msg.position[1])

    # send an int angle to move the servo position to 0-180  
    yaw_servo.publish(yaw_servo_position)
    pitch_servo.publish(pitch_servo_position)

if __name__ == "__main__":
    rospy.init_node("head_mover")
    
    # setup topics to control into arduino servo angles
    # publishing a integer between angle 0-180 /servo1 or /servo2 
    yaw_servo   = rospy.Publisher("servo1", UInt16, queue_size=1)
    pitch_servo = rospy.Publisher("servo2", UInt16, queue_size=1)

    # waiting for a JointState data on the topic "/move_head"



    # example data 
    #  DOCS for joint state
    # http://wiki.ros.org/joint_state_publisher
    
    # Data format
    # http://docs.ros.org/en/api/sensor_msgs/html/msg/JointState.html

    # Header header
    # string[] name  <- optional
    # float64[] position
    # float64[] velocity
    # float64[] effort

    # rostopic pub /move_head "/{header:{}, name: ['servo1', 'servo2'], position: [0.5, 0.5], velocity:[], effort:[]}""
    sub=rospy.Subscriber("move_head", JointState, move_servos)
    
    rate=rospy.Rate(10)
    
    print("servo_mover: Running")
    while not rospy.is_shutdown():
        rate.sleep()
    
#!/usr/bin/env python

# creates a ros node that controls two servo motors
#    on a arduino running ros serial 
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20210224



import rospy

from std_msgs.msg from String, Float32

motor1_position = 0.0
# just prints the current positions of the motors
def motor_positions_callback(msg):
    print(msg.data)

if __main__ =="__main__":
    rospy.init_node("servo_mover")

    pub=rospy.Publisher("head_servo_position", Float32, queue_size=1)

    while not rospy.is_shutdown():
        if motor1_position > 180:
            motor1_position = 0
        pub.publish(motor1_position)
        motor1_position += 0.01
        
        rate.sleep()
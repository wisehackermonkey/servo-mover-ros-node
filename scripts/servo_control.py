#!/usr/bin/env python3

# creates a ros node that controls two servo motors
#    on a arduino running ros serial 
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20210224



import rospy

from std_msgs.msg import String, Float32

motor1_position = 0.0
# just prints the current positions of the motors
def motor_positions_callback(msg):
    print(msg.data)

if __name__ == "__main__":
    rospy.init_node("servo_mover")

    pub=rospy.Publisher("head_servo_position", Float32, queue_size=1)
    # sub=rospy.Subscriber("")
    rate=rospy.Rate(10)
    print("servo_mover: Running")
    while not rospy.is_shutdown():
        if motor1_position > 180:
            motor1_position = 0
        pub.publish(motor1_position)
        motor1_position += 0.5
        
        rate.sleep()
#!/usr/bin/env python3

# creates a ros node that controls two servo motors
#    on a arduino running ros serial 
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20210224



import rospy

from std_msgs.msg import String, UInt16

motor1_position = 0
# just prints the current positions of the motors
def motor_positions_callback(msg):
    print(msg.data)

if __name__ == "__main__":
    rospy.init_node("servo_mover")

    pub=rospy.Publisher("servo", UInt16, queue_size=1)
    # sub=rospy.Subscriber("")
    rate=rospy.Rate(10)
    print("servo_mover: Running")
    while not rospy.is_shutdown():
        if motor1_position > 180:
            motor1_position = 0
        pub.publish(motor1_position)
        motor1_position += 1
        
        rate.sleep()
# [std_msgs/UInt16] vs. 
# [std_msgs/Int16]{'callerid': '/serial_node', 'md5sum': '1df79edf208b629fe6b81923a544552d', 'message_definition': 'uint16 data\n', 'tcp_nodelay': '0', 'topic': '/servo', 'type': 'std_msgs/UInt16'}
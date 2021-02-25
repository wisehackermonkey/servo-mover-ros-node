/*
 * Controlling ros arduino node to control 2 servo motors
 * by oran collins
 * github.com/wisehackermonkey
 * oranbusiness@gmail.com
 * 20210224
 * This sketch demonstrates the control of hobby R/C servos
 * using ROS and the arduiono
 * 
 * For the full tutorial write up, visit
 * www.ros.org/wiki/rosserial_arduino_demos
 *
 * For more information on the Arduino Servo Library
 * Checkout :
 * http://www.arduino.cc/en/Reference/Servo
 */

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/Float32.h>
#include <std_msgs/String.h>

String HEAD_SEND_TOPIC = "debug_head_position";
String HEAD_RECEIVE_TOPIC = "head_servo_position";

ros::NodeHandle  nh;

std_msgs:String debug_message;

Servo servo;

void servo_cb( const std_msgs::Float32& cmd_msg){
  servo.write(cmd_msg.data); //set servo angle, should be from 0-180  
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}



ros::Subscriber<std_msgs::Float32> sub(HEAD_RECEIVE_TOPIC, servo_cb);
// allow sending data back to computer for debugging purposes on ros topic "head_debug"
ros::Publisher debug_position(HEAD_SEND_TOPIC, &debug_message);

void setup(){
  Serial.begin(115200);
  pinMode(13, OUTPUT);

  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(debug_message);
  Serial.println("Setarting Ros Node Servo Control");
  debug_message.data = "Works!";
  servo.attach(9); //attach it to pin 9
}

void loop(){
  
  debug_position.publish(&debug_message);
  nh.spinOnce();
  delay(1);
}


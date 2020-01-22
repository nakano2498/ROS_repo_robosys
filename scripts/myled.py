#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
#cb =  rospy.loginfo(message.data)
def callback(data):
  flag = data.data
  if flag == 1:
    GPIO.output(24, GPIO.HIGH)
  elif flag != 1:
    GPIO.output(24, GPIO.LOW)
    

while not rospy.is_shutdown():
  rospy.init_node('myled')
  sub = rospy.Subscriber('robosys', Int32, callback)
  rospy.spin()
GPIO.cleanup()

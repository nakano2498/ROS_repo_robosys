#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

rospy.init_node('button_pub')
pub = rospy.Publisher('robosys', Int32, queue_size=1)
rate = rospy.Rate(10)
x = 0
while not rospy.is_shutdown():
    n = GPIO.input(14)
    print(n)
    if n == GPIO.HIGH:
        x = 1
        pub.publish(x)
    else:
        x = 0
        pub.publish(x)
    rate.sleep()
GPIO.cleanup()

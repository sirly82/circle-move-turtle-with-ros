#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_circle():
    rospy.init_node('circle_turtle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz
    
    vel_msg = Twist()
    vel_msg.linear.x = 2.0  # Kecepatan maju
    vel_msg.angular.z = 1.0  # Kecepatan rotasi

    while not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_circle()
    except rospy.ROSInterruptException:
        pass

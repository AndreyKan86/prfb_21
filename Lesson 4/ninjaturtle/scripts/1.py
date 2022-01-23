#!/usr/bin/env python

import math

import rospy

from geometry_msgs.msg import Twist

def main(lenght, angular):
  rospy.init_node('ninjaturtle', anonymous = True)
  pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
  rate = rospy.Rate(1.0)
  turtle = Twist()

  while True:
      pub.publish(movement(turtle, x=lenght))
      rate.sleep()
      pub.publish(movement(turtle, teta=angular))
      rate.sleep()

def movement (turtle, x=0, y=0, z=0, phi=0, psi=0, teta=0):
    turtle.linear.x = x
    turtle.linear.y = y
    turtle.linear.z = z

    turtle.angular.x = phi
    turtle.angular.y = psi
    turtle.angular.z = teta
    return turtle
  


  

if __name__ == '__main__':
    try:
        lenght = 5.0
        angular = math.pi/2
        main(lenght, angular)
    except rospy.ROSInterruptException:
        pass



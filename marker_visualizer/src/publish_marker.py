#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def talker():
        rospy.init_node('publisher',anonymous=True)
        pub=rospy.Publisher('my_topic',String,queue_size=10)
        rate=rospy.Rate(10)
        while not rospy.is_shutdown():
            message=String()
            message.data="hello world %s" % rospy.get_time()

            pub.publish(message)
            rate.sleep()

if __name__=='__main__':
        try:
            talker()
        except rospy.ROSInterruptException:
            pass


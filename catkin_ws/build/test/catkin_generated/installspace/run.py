import rospy
from std_msgs.msg import String
from time import sleep

rospy.init_node('run')
pub_ok = rospy.Publisher('pub_ok', String, queue_size=10)
sleep(2)
pub_ok.publish("ok")

import rospy	
import tf

if __name__ == '__main__':
	
	rospy.init_node('base_link_tf_broadcaster', anonymous=True)
	
	br = tf.TransformBroadcaster()
	rate = rospy.Rate(10.0)
	
	while not rospy.is_shutdown():
		
		br.sendTransform((0, 0, 3.4), (0.0, 0.0, 0.0, 1.0), rospy.Time.now(), "base_link", "base_footprint")
		
		rate.sleep()

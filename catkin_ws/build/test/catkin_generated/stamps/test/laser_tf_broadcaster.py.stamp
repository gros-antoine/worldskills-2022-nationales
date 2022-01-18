import rospy	
import tf

if __name__ == '__main__':
	
	rospy.init_node('laser_tf_broadcaster', anonymous=True)
	
	br = tf.TransformBroadcaster()
	rate = rospy.Rate(10.0)
	
	while not rospy.is_shutdown():
		
		br.sendTransform((1.15, 0, 17.3), (0.0, 0.0, 0.0, 1.0), rospy.Time.now(), "lidar", "base_link")
		
		rate.sleep()

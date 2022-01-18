import rospy	
import tf

if __name__ == '__main__':
	
	rospy.init_node('imu_tf_broadcaster', anonymous=True)
	
	br = tf.TransformBroadcaster()
	rate = rospy.Rate(10.0)
	
	while not rospy.is_shutdown():
		
		br.sendTransform((9.5, 0, 6), (0.0, 0.0, 0.0, 1.0), rospy.Time.now(), "imu", "base_link")
		
		rate.sleep()

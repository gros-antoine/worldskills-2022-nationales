#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Quaternion, Vector3
from sensor_msgs.msg import Imu
from test.msg import IMU
from math import pi, sqrt, cos, sin, asin
from tf.transformations import quaternion_from_euler

pub_imu_data = rospy.Publisher('imu_data', Imu, queue_size=10)

def callback_imu(msg):
	
	# Recuperation des mesures de l'imu
	angle_x = msg.angle_x
	angle_y = msg.angle_y
	angle_z = msg.angle_z
	gyr_x = msg.gyr_x
	gyr_y = msg.gyr_y
	gyr_z = msg.gyr_z
	acc_x = msg.acc_x
	acc_y = msg.acc_y
	acc_z = msg.acc_z	
	
	# Creation d'un vecteur acceleration lineaire
	linear_acc = Vector3()
	linear_acc.x = acc_x * 9.81
	linear_acc.y = acc_y * 9.81
	linear_acc.z = acc_z * 9.81
	
	# Creation d'un vecteur vitesse angulaire
	angular_vel = Vector3()
	angular_vel.x = gyr_x
	angular_vel.y = gyr_y
	angular_vel.z = gyr_z
	
	# Calcul du quaternion d'orientation
	quaternion = Quaternion()
	
	coord = quaternion_from_euler(angle_x, angle_y, angle_z)
	norme = sqrt(coord[0] * coord[0] + coord[1] * coord[1] + coord[2] * coord[2] + coord[3] * coord[3])
	quaternion.x = coord[0] / norme
	quaternion.y = coord[1] / norme
	quaternion.z = coord[2] / norme
	quaternion.w = coord[3] / norme
	
	# Covariance des 3 proprietes precedentes (0 partout car on n'a pas 
	# lol)
	covariance =  [0] * 9
	
	# Creation d'un message de type Imu
	imu = Imu()
	imu.header.stamp = rospy.Time.now()
	imu.header.frame_id = "imu"
	imu.orientation = quaternion
	imu.angular_velocity = angular_vel
	imu.linear_acceleration = linear_acc
	imu.orientation_covariance = [1e6, 0, 0, 0, 1e6, 0, 0, 0, 1e-6]
	imu.angular_velocity_covariance = [1e6, 0, 0, 0, 1e6, 0, 0, 0, 1e-6]
	imu.linear_acceleration_covariance = [-1, 0, 0, 0, 0, 0, 0, 0, 0]
	#imu.orientation_covariance = covariance
	#imu.angular_velocity_covariance = covariance
	#imu.linear_acceleration_covariance = covariance
	
	# Publication du message sur le topic lu par ros_pose_ekf
	pub_imu_data.publish(imu)
	
	# Utilise par Florent Chretien
	# Donne des resultats significativement different de la methode 
	# precedente
	'''# Calcul initial du quaternion
	if(first_data):
	  
		last_time = time()
	  
		first_data = False
	  
		# Calcul a partir des angles deduits des accelerations
		angle_x_quat = -asin(acc_y / acc_norme)
		angle_y_quat = asin(acc_x / acc_norme)
		angle_z_quat = 0
	  
		coord = get_quaternion(angle_x_quat, angle_y_quat, angle_z_quat)
		quaternion.x = coord[0]
		quaternion.y = coord[1]
		quaternion.z = coord[2]
		quaternion.w = coord[3]
	
	# Calcul utilise le reste du temps
	else:
	  
		dt = time() - last_time
		last_time = time()
	  
		# Filtrage des données (grave bizarre mais bon)
		filter_coefficient = 0.5 / (0.5 + dt)
		angle_x_quat = angle_x_quat * filter_coefficient + angle_x * (1 - filter_coefficient)
		angle_y_quat = angle_y_quat * filter_coefficient + angle_y * (1 - filter_coefficient)
		angle_z_quat = angle_z
	  
		coord = get_quaternion(angle_x_quat, angle_y_quat, angle_z_quat)
		quaternion.x = coord[0]
		quaternion.y = coord[1]
		quaternion.z = coord[2]
		quaternion.w = coord[3]'''

		
# Initialisation du node et des subscribers
def listener():
	
	# Initialisation de ce node
	rospy.init_node('lidar_imu_node', anonymous=True)
	
	# Abonnement au  topic imu_raw pour recuperer les donnees de l'imu
	rospy.Subscriber('imu_raw', IMU, callback_imu)
	
	rospy.spin()


if __name__ == '__main__':
	
	try:
		listener()
	except:
		pass



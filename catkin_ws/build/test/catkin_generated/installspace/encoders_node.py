#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Pose, PoseWithCovariance, Vector3, Twist, TwistWithCovariance
from tf.transformations import quaternion_from_euler
from numpy import sign
from math import pi, cos, sin, sqrt
from time import time
from test.msg import Encoders

pub_wheel_odom = rospy.Publisher('odom', Odometry, queue_size=10)

# Infos sur le robot
rayon_roue = 0.0315           					 # Rayon roue du robot
nbr_puls_roue = 410.189								 # Nombre pulsation encodeur roue
nbr_puls_robot = 1427.5							 # Nombre pulsation pour faire un tour de robot sur lui-meme

dist_puls = rayon_roue * 2 * pi / nbr_puls_roue  # Distance parcourue pour une impulsion d'encodeur
angle_puls = 2 * pi / nbr_puls_robot			 # Angle parcouru (du robot) pour une impulsion d'encodeur 

last_pos_droit = 0.0
last_pos_gauche = 0.0

last_time = 0.0

pos_x = 0.0
pos_y = 0.0

vel_x = 0.0
vel_y = 0.0

angle_z = 0.0
ang_vel_z = 0.0

# Pour les calculs de covariances
# Incertitudes :
D_rayon_roue = 0.001
D_nbr_puls_roue = 5
D_nbr_puls_robot = 20	# 5 * 4 car j'ai mesure le nombre de puls pour 90°
D_dt = 0.0000001		# Precision de la librairie time (plus petit chiffre apres la virgule, a voir si c'est utile)
D_dist_puls = D_rayon_roue * 2 * pi / nbr_puls_roue + rayon_roue * 2 * pi * D_nbr_puls_roue / (nbr_puls_roue * nbr_puls_roue)
D_angle_puls = 2 * pi * D_nbr_puls_robot / (nbr_puls_robot * nbr_puls_robot)

#covariance_pos = [0] * 36
covariance_pos = [1e-8, 0, 0, 0, 0, 0,
				  0, 1e-8, 0, 0, 0, 0,
				  0, 0, 1e6, 0, 0, 0,
				  0, 0, 0, 1e6, 0, 0,
				  0, 0, 0, 0, 1e6, 0,
				  0, 0, 0, 0, 0, 1e-8]
#covariance_vel = [0] * 36
covariance_vel = [1e-8, 0, 0, 0, 0, 0,
				  0, 1e-8, 0, 0, 0, 0,
				  0, 0, 1e6, 0, 0, 0,
				  0, 0, 0, 1e6, 0, 0,
				  0, 0, 0, 0, 1e6, 0,
				  0, 0, 0, 0, 0, 1e-8]

def callback_encoders(msg):
	
	global covariance_pos
	global covariance_vel
	
	global last_pos_droit
	global last_pos_gauche
	
	global last_time
	
	global pos_x
	global pos_y
	
	global vel_x
	global vel_y
	
	global angle_z
	global ang_vel_z
	
	dt = time() - last_time
	last_time = time()
	
	pos_droit = msg.angular_pose_droit
	pos_gauche = msg.angular_pose_gauche
	
	delta_pos_droit = pos_droit - last_pos_droit
	delta_pos_gauche = - pos_gauche - last_pos_gauche    # Car moteur dans l'autre sens donc negatif
			
	last_pos_droit = pos_droit
	last_pos_gauche = - pos_gauche
	
	# Pour les calculs
	distance = 0.0
	
	# Incertitudes, initialisation pour plus tard
	D_distance = 0.0
	D_angle_z = 0.0
	
	# rotation
	if(not sign(delta_pos_droit) == sign(delta_pos_gauche)):
		
		#print("rotation")
		
		last_angle = angle_z
		
		angle = (delta_pos_droit - delta_pos_gauche) * angle_puls / 2  # moyenne des deux rotations, utile ?
		angle_z += angle
		
		ang_vel_z = (angle_z - last_angle) / dt
		
		# Incertitude sur l'angle
		D_angle_z = (delta_pos_droit - delta_pos_gauche) * D_angle_puls / 2
		
	# translation
	else:
		
		#print("translation")
		
		distance = (delta_pos_droit + delta_pos_gauche) * dist_puls / 2 # moyenne des deux avancements, utile ?
		
		last_pos_x = pos_x
		last_pos_y = pos_y
		
		pos_x += cos(angle_z) * distance
		pos_y += sin(angle_z) * distance
		
		vel_x = (pos_x - last_pos_x) / dt
		vel_y = (pos_y - last_pos_y) / dt
		
		ang_vel_z = 0.0
		
		# Incertitude sur la distance
		D_distance = (delta_pos_droit + delta_pos_gauche) * D_dist_puls / 2
	
	# Calcul des matrices de covariance (variance en fait car covariance d'une valeur avec elle-meme)
	
	# Matrice des covariances des positions
	# Covariance de la position en x
	covariance_pos[0] += (cos(angle_z) * D_distance + distance * D_angle_z * sin(angle_z))**2
	# Covariance de la position en y
	covariance_pos[7] += (sin(angle_z) * D_distance + distance * D_angle_z * cos(angle_z))**2
	'''# Covariance de la position en z (pas d'estimation donc on suppose tres peu d'erreur)
	covariance_pos[14] = 1e6
	# Covariance de la position angulaire autour de x (pas d'estimation donc on suppose tres peu d'erreur)
	covariance_pos[21] = 1e6
	# Covariance de la position angulaire autour de y (pas d'estimation donc on suppose tres peu d'erreur)
	covariance_pos[28] = 1e6'''
	# Covariance de la position angulaire autour de z
	covariance_pos[35] += D_angle_z * D_angle_z
	
	# Matrice des covariances des vitesses
	# Covariance de la vitesse en x
	covariance_vel[0] = (2 * (cos(angle_z) * D_distance + distance * D_angle_z * sin(angle_z)) / dt + D_dt * vel_x / dt)**2
	# Covariance de la vitesse en y
	covariance_vel[7] = (2 * (sin(angle_z) * D_distance + distance * D_angle_z * cos(angle_z)) / dt + D_dt * vel_y / dt)**2
	'''# Covariance de la vitesse en x
	covariance_vel[0] = (2 * sqrt(covariance_pos[0]) / dt + D_dt * vel_x / dt)**2
	# Covariance de la vitesse en y
	covariance_vel[7] = (2 * sqrt(covariance_pos[7]) / dt + D_dt * vel_y / dt)**2'''
	'''# Covariance de la vitesse en z (pas d'estimation donc on suppose tres peu d'erreur)
	covariance_vel[14] = 1e6
	# Covariance de la vitesse angulaire autour de x (pas d'estimation donc on suppose tres peu d'erreur)
	covariance_vel[21] = 1e6
	# Covariance de la vitesse angulaire autour de y (pas d'estimation donc on suppose tres peu d'erreur)
	covariance_vel[28] = 1e6'''
	# Covariance de la vitesse angulaire autour de z
	covariance_vel[35] = (2 * D_angle_z / dt + D_dt * ang_vel_z / dt)**2
	
	'''covariance_pos = [1e-3, 0, 0, 0, 0, 0,
					  0, 1e-3, 0, 0, 0, 0,
					  0, 0, 1e6, 0, 0, 0,
					  0, 0, 0, 1e6, 0, 0,
					  0, 0, 0, 0, 1e6, 0,
					  0, 0, 0, 0, 0, 1e3]
					  
	covariance_vel = [1e-3, 0, 0, 0, 0, 0,
					  0, 1e-3, 0, 0, 0, 0,
					  0, 0, 1e6, 0, 0, 0,
					  0, 0, 0, 1e6, 0, 0,
					  0, 0, 0, 0, 1e6, 0,
					  0, 0, 0, 0, 0, 1e3]'''
					  
	
	odom = Odometry()
	odom.header.stamp = rospy.Time.now()
	odom.header.frame_id = "odom"
	odom.child_frame_id = "base_link"
	
	pose = Pose()
	pose.position = Point(pos_x, pos_y, 0.0)
	quaternion = quaternion_from_euler(0, 0, angle_z)
	norme = sqrt(quaternion[0] * quaternion[0] + quaternion[1] * quaternion[1] + quaternion[2] * quaternion[2] + quaternion[3] * quaternion[3])
	pose.orientation.x = quaternion[0] / norme
	pose.orientation.y = quaternion[1] / norme
	pose.orientation.z = quaternion[2] / norme
	pose.orientation.w = quaternion[3] / norme
	odom.pose.pose = pose
	odom.pose.covariance = covariance_pos
	
	twist = Twist()
	twist.linear = Vector3(vel_x, vel_y, 0)
	twist.angular = Vector3(0, 0, ang_vel_z)
	odom.twist.twist = twist
	odom.twist.covariance = covariance_vel
	
	pub_wheel_odom.publish(odom)
	

def listener():
	
	rospy.init_node('encoders_node', anonymous=True)
	
	rospy.Subscriber('pub_encoders', Encoders, callback_encoders)
	
	rospy.spin()

if __name__ == '__main__':
	
	try:
		listener()
	except:
		pass

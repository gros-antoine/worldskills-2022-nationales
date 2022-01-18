import rospy
from std_msgs.msg import String, Float32MultiArray
from test.msg import Encoders, Moteurs, IMU
from math import pi
from time import sleep

pub_ok = rospy.Publisher('pub_ok', String, queue_size=10)
pub_move = rospy.Publisher('pub_move', Moteurs, queue_size=10)

encoders_values = [0, 0]
moteurs = Moteurs()
rayon_roue = 0.0315 * 1000      # Rayon roue du robot en mm
nbr_puls_roue = 397			# Nombre pulsation pour faire un tour de robot sur lui-meme
vitesse_moteurs = 150			#vitesse des moteurs lors du déplacement linéaire du robot

current_angle = 0

def encoders_callback(data):
	global encoders_values
	encoders_values = [-data.angular_pose_gauche, data.angular_pose_droit]

def angle_callback(data):
	global current_angle
	current_angle = data.angle_z

def avancer_callback(data):
	global moteurs
	global vitesse_moteurs
	global encoders_values
	listener_encoders()
	listener_imu()
	ordre = data.data[1] * 2*pi / 360
	start_pose = [encoders_values[0], encoders_values[1]]
	nbr_puls_parc = data.data[0] / (2*pi*rayon_roue) * nbr_puls_roue #nombre de pulsation de roues à parcourir pour réaliser la distance mm
	final_pose = (encoders_values[0] + nbr_puls_parc + encoders_values[1] + nbr_puls_parc) / 2 #pose à atteindre en fin de mouvement
	#print(start_pose, final_pose)
	while True:
		moy_poses = (encoders_values[0] + encoders_values[1]) / 2 #nombre moyen de pulsation des roues
		sleep(0.050)
		if moy_poses >= final_pose:
			moteurs.moteur_droit = 0
			moteurs.moteur_gauche = 0
			pub_move.publish(moteurs)
			pub_ok.publish("ok")
			return None
		else:
			moteurs.moteur_droit = vitesse_moteurs
			moteurs.moteur_gauche = vitesse_moteurs
			if current_angle != 0:	
				if current_angle >= ordre + 0.0087: #0.25 deg en rad
					moteurs.moteur_droit = 0
				if current_angle <= ordre - 0.00436:
					moteurs.moteur_gauche = 0
			pub_move.publish(moteurs)
		listener_encoders()
		listener_imu()



def listener_encoders():
	rospy.Subscriber("pub_encoders", Encoders, encoders_callback)

def listener_imu():
	rospy.Subscriber("pub_imu", IMU, angle_callback)

def listener(var):
	rospy.init_node('programme_avancer2')
	rospy.Subscriber("pub_avancer2", Float32MultiArray, avancer_callback)
	if var:
		rospy.spin()


if __name__ == '__main__':
	try:
		listener(1)
	except:
			pass

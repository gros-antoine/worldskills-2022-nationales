import rospy
from std_msgs.msg import String
from test.msg import Encoders, Moteurs
from math import pi
from time import sleep

pub_ok = rospy.Publisher('pub_ok', String, queue_size=10)
pub_move = rospy.Publisher('pub_move', Moteurs, queue_size=10)

encoders_values = [0, 0]
moteurs = Moteurs()
rayon_roue = 0.0315 * 1000      # Rayon roue du robot en mm
nbr_puls_roue = 403			# Nombre pulsation pour faire un tour de robot sur lui-meme
vitesse_moteurs = -60			#vitesse des moteurs lors du déplacement linéaire du robot


def encoders_callback(data):
	global encoders_values
	encoders_values = [-data.angular_pose_gauche, data.angular_pose_droit]

def avancer_callback(data):
	global moteurs
	global vitesse_moteurs
	global encoders_values
	listener_encoders()
	start_pose = [encoders_values[0], encoders_values[1]]
	nbr_puls_parc = int(data.data) / (2*pi*rayon_roue) * nbr_puls_roue #nombre de pulsation de roues à parcourir pour réaliser la distance mm
	final_pose = (encoders_values[0] - nbr_puls_parc + encoders_values[1] - nbr_puls_parc) / 2 #pose à atteindre en fin de mouvement
	#print(start_pose, final_pose)
	while True:
		moy_poses = (encoders_values[0] + encoders_values[1]) / 2 #nombre moyen de pulsation des roues
		sleep(0.050)
		if moy_poses <= final_pose:
			moteurs.moteur_droit = 0
			moteurs.moteur_gauche = 0
			pub_move.publish(moteurs)
			pub_ok.publish("ok")
			return None
		else:
			moteurs.moteur_droit = vitesse_moteurs
			moteurs.moteur_gauche = vitesse_moteurs
			pub_move.publish(moteurs)
		listener_encoders()



def listener_encoders():
	rospy.Subscriber("pub_encoders", Encoders, encoders_callback)


def listener(var):
	rospy.init_node('programme_reculer')
	rospy.Subscriber("pub_reculer", String, avancer_callback)
	if var:
		rospy.spin()


if __name__ == '__main__':
	try:
		listener(1)
	except:
			pass
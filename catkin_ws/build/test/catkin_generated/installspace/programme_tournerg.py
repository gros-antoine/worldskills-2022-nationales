import rospy
from std_msgs.msg import String
from test.msg import IMU, Moteurs
from math import pi
from time import sleep

pub_ok = rospy.Publisher('pub_ok', String, queue_size=10)
pub_move = rospy.Publisher('pub_move', Moteurs, queue_size=10)

moteurs = Moteurs()
vitesse_moteurs = 150			#vitesse des moteurs lors du déplacement linéaire du robot
imu_value = 0

ok = 0

def imu_callback(data):
	global imu_value
	imu_value = round(data.angle_z, 3)

def tourner_callback(data):
	global moteurs
	global vitesse_moteurs
	global imu_value
	global ok
	listener_imu()
	start_pose = imu_value
	final_pose = round(imu_value + (float(data.data) * 2*pi / 360), 3)
	while True:
		curent_poses = imu_value
		sleep(0.050)
		if curent_poses >= final_pose:
			moteurs.moteur_droit = 0
			moteurs.moteur_gauche = 0
			pub_move.publish(moteurs)
			for i in range(1):
				sleep(1)
				listener_imu()
				while ok:
					curent_poses = imu_value
					if curent_poses <= final_pose + 0.005 and curent_poses >= final_pose -0.005:
						moteurs.moteur_droit = 0
						moteurs.moteur_gauche = 0
						pub_move.publish(moteurs)
						break
					if curent_poses >= final_pose:
						moteurs.moteur_droit = -100
						moteurs.moteur_gauche = 100
						pub_move.publish(moteurs)
					if curent_poses < final_pose:
						moteurs.moteur_droit =  100
						moteurs.moteur_gauche = -100
						pub_move.publish(moteurs)
					sleep(0.01)
					listener_imu()
			ok = 1				
			pub_ok.publish("ok")
			return None
		else:
			moteurs.moteur_droit = vitesse_moteurs
			moteurs.moteur_gauche = -vitesse_moteurs
			pub_move.publish(moteurs)
		listener_imu()



def listener_imu():
	rospy.Subscriber("pub_imu", IMU, imu_callback)

def listener(var):
	rospy.init_node('programme_tournerg')
	rospy.Subscriber("pub_tournerg", String, tourner_callback)
	if var:
		rospy.spin()


if __name__ == '__main__':
	try:
		listener(1)
	except:
			pass
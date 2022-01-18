import rospy
from std_msgs.msg import String, Float32
from test.msg import Moteurs, IMU
from time import sleep
from math import pi

current_angle = 0
moteurs = Moteurs()

pub_ok = rospy.Publisher('pub_ok', String, queue_size=10)
pub_move = rospy.Publisher('pub_move', Moteurs, queue_size=10)

def angle_callback(data):
	global current_angle
	current_angle = data.angle_z


def callback(data):
	global current_angle
	global moteur
	listener_imu()
	ordre = (float(data.data) * 2*pi / 360)
	while True:
		if current_angle <= ordre + 0.005 and current_angle >= ordre - 0.005:
			moteurs.moteur_droit = 0
			moteurs.moteur_gauche = 0
			pub_move.publish(moteurs)
			break
		if current_angle != 0:	
			if current_angle >= ordre:
				moteurs.moteur_gauche = 100
				pub_move.publish(moteurs)
			else:
				moteurs.moteur_droit = 100
				pub_move.publish(moteurs)
		listener_imu()
		sleep(0.01)
	pub_ok.publish("ok")

def listener_imu():
	rospy.Subscriber("pub_imu", IMU, angle_callback)

def listener():
	rospy.init_node('verif_angle')
	rospy.Subscriber("pub_verifangle", String, callback)
	rospy.spin()


if __name__ == '__main__':
	try:
		listener()
	except:
			pass
import rospy
from std_msgs.msg import String, Float32
from test.msg import Moteurs
from time import sleep


current_distance = 0 #valeur de la distance en permanance
moteurs = Moteurs()

pub_ok = rospy.Publisher('pub_ok', String, queue_size=10)
pub_move = rospy.Publisher('pub_move', Moteurs, queue_size=10)

def distance_callback(data):
	global current_distance
	current_distance = round(data.data, 4)


def callback(data):
	global current_distance
	global moteur
	listener_ultrason()
	ordre = float(data.data)
	while True:
		if current_distance >= ordre - 1 and current_distance <= ordre + 1:
			moteurs.moteur_droit = 0
			moteurs.moteur_gauche = 0
			pub_move.publish(moteurs)
			break
		if current_distance >= ordre:
			moteurs.moteur_droit = 100
			moteurs.moteur_gauche = 100
			pub_move.publish(moteurs)
		if current_distance < ordre:
			moteurs.moteur_droit = -100
			moteurs.moteur_gauche = -100
			pub_move.publish(moteurs)
		listener_ultrason()
		sleep(0.01)
	pub_ok.publish("ok")





def listener_ultrason():
	rospy.Subscriber("pub_distance", Float32, distance_callback)

def listener():
	rospy.init_node('verif_distance')
	rospy.Subscriber("pub_verifdistance", String, callback)
	rospy.spin()


if __name__ == '__main__':
	try:
		listener()
	except:
			pass
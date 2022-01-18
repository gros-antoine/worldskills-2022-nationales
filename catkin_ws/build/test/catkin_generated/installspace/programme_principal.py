import rospy
from std_msgs.msg import String, Float32MultiArray
from time import sleep

pub_avancer = rospy.Publisher('pub_avancer', Float32MultiArray, queue_size=10)
pub_reculer = rospy.Publisher('pub_reculer', String, queue_size=10)
pub_tournerg = rospy.Publisher('pub_tournerg', String, queue_size=10)
pub_tournerd = rospy.Publisher('pub_tournerd', String, queue_size=10)
pub_verifdistance = rospy.Publisher('pub_verifdistance', String, queue_size=10)
pub_verifangle = rospy.Publisher('pub_verifangle', String, queue_size=10)
pub_fin = rospy.Publisher('pub_fin', String, queue_size=10)
pub_camera = rospy.Publisher('pub_camera', String, queue_size=10)
pub_signal = rospy.Publisher('pub_signal', String, queue_size=10)


global_indentation = 0

array_avancer = Float32MultiArray()
array_avancer.data = [0, 0]

def avancer(mm, angle):
	sleep(1)
	array_avancer.data[0], array_avancer.data[1] = mm, angle
	pub_avancer.publish(array_avancer)

def reculer(mm):
	sleep(1)
	pub_reculer.publish(str(mm))

def tourner_a_gauche(angle):
	sleep(1)
	pub_tournerg.publish(str(angle))

def tourner_a_droite(angle):
	sleep(1)
	pub_tournerd.publish(str(angle))

def verifier_angle(angle):
	sleep(1)
	pub_verifangle.publish(str(angle))

def verifier_distance(mm):
	sleep(1)
	pub_verifdistance.publish(str(mm))

def camera(cam):
	sleep(1)
	pub_camera.publish(cam)

def signal(msg):
	sleep(1)
	pub_signal.publish(msg)

'''	'''

def global_callback(data):
	
	global global_indentation

	tableau_principal = [[avancer, [0, 0]], [reculer, [0]], [tourner_a_droite, [0]], [tourner_a_gauche, [0]],  #initialisation A NE PAS RETIRER
	[avancer, [500, 0]],
	[verifier_distance, [20]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [90]],
	[avancer, [800, 90]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [180]],
	[avancer, [1400, 180]],
	[verifier_distance, [20]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [270]],
	[avancer, [1700, 270]],
	[verifier_distance, [30]],
	[tourner_a_droite, [90]],
	[verifier_angle, [180]],
	[verifier_distance, [20]],
	[verifier_angle, [180]],
	[camera, ["1"]], #verification de la couleur
	[signal, ["1"]],
	[verifier_distance, [25]],
	[tourner_a_droite, [90]], #attention prendre de la marge
	[verifier_angle, [90]],
	[reculer, [150]],
	#avancer en fonction du resultat de la cam
	[camera, ["2"]],
	[tourner_a_droite, [360]],
	[verifier_angle, [-270]],
	#avancer en fonction de ce qu'il reste à parcourir
	[camera, ["3"]],
	[avancer, [1600, -270]],
	[verifier_distance, [37]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [-180]],
	[verifier_distance, [25]],
	[camera, ["1"]],
	[signal, ["1"]],
	[verifier_distance, [35]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [-90]],
	[avancer, [1500, -90]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [0]],
	[avancer, [1100, 0]],
	[tourner_a_droite, [90]],
	[verifier_angle, [-90]],
	[avancer, [650+900, -90]],
	[verifier_distance, [30]],
	[tourner_a_droite, [90]],
	[verifier_angle, [-180]],
	[camera, ["4"]], #aller à la gom de la bonne couleur sauf rouge
	[camera, ["5"]], #aller a la gom rouge ou rester sur place*
	[camera, ["6"]], #avancer jusqu'a gom rouge
	[tourner_a_droite, [360]],
	[camera, ["7"]], # verif angle
	[camera, ["8"]], #revenir sur la gom jaune si on etait sur la rouge
	[camera, ["9"]], # reorientation si on est sur le rouge
	[verifier_angle, [-540]],
	[verifier_distance, [25]],
	[tourner_a_droite, [180]],
	[verifier_angle, [-720]],
	[avancer, [290+300, -720]],
	[verifier_distance, [25]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [-630]],
	[avancer, [850, -630]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [-540]],
	[avancer, [500, 540]]]



	try:
		tableau_principal[global_indentation][0](*tableau_principal[global_indentation][1])
		print(global_indentation)
		global_indentation += 1
	except:
		print("fin")
		pub_fin.publish("fin")







def listener():
	rospy.init_node('programme_principal')
	rospy.Subscriber("pub_ok", String, global_callback)
	rospy.spin()



if __name__ == '__main__':
	try:
		listener()
	except:
		pass


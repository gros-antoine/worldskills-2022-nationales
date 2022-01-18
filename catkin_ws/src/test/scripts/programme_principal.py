import rospy
from std_msgs.msg import String, Float32MultiArray
from time import sleep

pub_avancer = rospy.Publisher('pub_avancer', Float32MultiArray, queue_size=10)
pub_avancer2 = rospy.Publisher('pub_avancer', Float32MultiArray, queue_size=10)
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

def avancer2(mm, angle):
	sleep(1)
	array_avancer.data[0], array_avancer.data[1] = mm, angle
	pub_avancer2.publish(array_avancer)


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



'''[tourner_a_droite, [90]],
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
	[camera, ["10"]],
	[verifier_distance, [25]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [-630]],
	[avancer, [900, -630]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [-540]],
	[avancer, [500, -540]]]'''

'''[avancer, [500, 0]],
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
	#avancer en fonction du resultat de la cam
	[avancer, [1400-150, 90]],
	#avancer en fonction de ce qu'il reste à parcourir
	[tourner_a_gauche, [90]],
	[verifier_angle, [180]],
	[verifier_distance, [30+13.5-11]],
	[tourner_a_droite, [90]],
	[verifier_angle, [90]],
	[avancer2, [1600, 90]],
	[verifier_distance, [35]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [180]],
	[verifier_distance, [25]],
	[camera, ["2"]],
	[signal, ["1"]],
	[verifier_distance, [35]],
	[tourner_a_droite, [270]],
	[verifier_angle, [-90]],
	[avancer2, [1500, -90]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [0]],
	[avancer, [1100, 0]],
	[verifier_distance, [19]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [90]],
	[avancer, [650, 90]], #potentiellement 700-110 ou plus faible que 700
	[verifier_distance, [41-11]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [180]],
	[avancer, [950-250-110, 180]],
	[verifier_distance, [25]],
	[camera, ["3"]],
	[signal, ["1"]],
	[tourner_a_droite, [180]],
	[verifier_angle, [0]],
	[avancer, [950-250-110, 0]],
	[verifier_distance, [19]],
	[tourner_a_droite, [90]],
	[verifier_angle, [-90]],
	[avancer, [1500, -90]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [0]],
	[verifier_distance, [19]],
	[tourner_a_droite, [90]],
	[verifier_angle, [-90]],
	[avancer2, [1240-110-140, -90]],
	[verifier_distance, [14]],
	[tourner_a_droite, [90]],
	[verifier_angle, [-180]],'''

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
	#avancer en fonction du resultat de la cam
	[avancer, [1400-150, 90]],
	#avancer en fonction de ce qu'il reste à parcourir
	[tourner_a_gauche, [90]],
	[verifier_angle, [180]],
	[verifier_distance, [30+13.5-11]],
	[tourner_a_droite, [90]],
	[verifier_angle, [90]],
	[avancer2, [1600, 90]],
	[verifier_distance, [35]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [180]],
	[verifier_distance, [25]],
	[camera, ["2"]],
	[signal, ["1"]],
	[verifier_distance, [35]],
	[tourner_a_droite, [270]],
	[verifier_angle, [-90]],
	[avancer2, [1500, -90]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [0]],
	[avancer, [1100, 0]],
	[verifier_distance, [19]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [90]],
	[avancer, [650, 90]], #potentiellement 700-110 ou plus faible que 700
	[verifier_distance, [41-11]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [180]],
	[avancer, [950-250-110, 180]],
	[verifier_distance, [25]],
	[camera, ["3"]],
	[signal, ["1"]],
	[tourner_a_droite, [180]],
	[verifier_angle, [0]],
	[avancer, [950-250-110, 0]],
	[verifier_distance, [19]],
	[tourner_a_droite, [90]],
	[verifier_angle, [-90]],
	[avancer, [1500, -90]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [0]],
	[verifier_distance, [19]],
	[tourner_a_droite, [90]],
	[verifier_angle, [-90]],
	[avancer2, [1240-110-140, -90]],
	[verifier_distance, [14]],
	[tourner_a_droite, [90]],
	[verifier_angle, [-180]],
	[camera, ["4"]],
	[camera, ["5"]],
	[camera, ["6"]],
	[camera, ["7"]],
	[camera, ["8"]],
	[camera, ["9"]],
	[camera, ["10"]],
	[camera, ["11"]],
	[camera, ["12"]],
	[camera, ["13"]],
	[camera, ["14"]],
	[camera, ["15"]],
	[camera, ["16"]],
	[camera, ["17"]],
	[camera, ["18"]],
	[camera, ["19"]],
	[camera, ["20"]],
	[camera, ["21"]],
	[camera, ["22"]],
	[camera, ["23"]],
	[camera, ["24"]],
	[camera, ["25"]],
	[camera, ["26"]],
	[camera, ["27"]],
	[camera, ["28"]],
	[camera, ["29"]],
	[camera, ["30"]],
	[camera, ["31"]],
	[camera, ["32"]],
	[camera, ["33"]],
	[camera, ["34"]],
	[camera, ["35"]],
	[camera, ["36"]],
	[camera, ["37"]],
	[camera, ["38"]],
	[camera, ["39"]],
	[camera, ["40"]],
	[camera, ["41"]],
	[camera, ["42"]],
	[camera, ["43"]],
	[camera, ["44"]],
	[camera, ["45"]],
	[camera, ["46"]],
	[camera, ["47"]],
	[camera, ["48"]],
	[camera, ["49"]],
	[camera, ["50"]],
	[camera, ["51"]],
	[camera, ["52"]],
	[camera, ["53"]],
	[camera, ["54"]],
	[camera, ["55"]],
	[camera, ["56"]],
	[camera, ["57"]],
	[camera, ["58"]],
	[camera, ["59"]],
	[camera, ["60"]],
	[camera, ["61"]],
	[camera, ["62"]],
	[camera, ["63"]],
	[camera, ["64"]],
	[camera, ["65"]],
	[camera, ["66"]],
	[camera, ["67"]],
	[camera, ["68"]],
	[camera, ["69"]],
	[camera, ["70"]],
	[camera, ["71"]],
	[camera, ["72"]],
	[tourner_a_droite, [90]],
	[verifier_angle, [-270]],
	[avancer, [900, -270]],
	[tourner_a_gauche, [90]],
	[verifier_angle, [-180]],
	[avancer, [500, -180]]]


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


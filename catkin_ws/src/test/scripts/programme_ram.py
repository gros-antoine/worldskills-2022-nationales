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

def global_callback(data):
	global global_indentation

	tableau_principal = [[avancer, [0, 0]], [reculer, [0]], [tourner_a_droite, [0]], [tourner_a_gauche, [0]],  #initialisation A NE PAS RETIRER
	[verifier_distance, [10]]]


	try:
		tableau_principal[global_indentation][0](*tableau_principal[global_indentation][1])
	except:
		print("fin")
		pub_fin.publish("fin")



	print(global_indentation)
	global_indentation += 1



def listener():
	rospy.init_node('programme_principal')
	rospy.Subscriber("pub_ok", String, global_callback)
	rospy.spin()



if __name__ == '__main__':
	try:
		listener()
	except:
		pass


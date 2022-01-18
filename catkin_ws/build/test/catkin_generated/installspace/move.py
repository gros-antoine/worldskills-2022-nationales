import rospy
from test.msg import Moteurs, Encoders

pub = rospy.Publisher('chatter_move', Moteurs, queue_size=10)4

moteurs = Moteurs()
rayon_roue = 0.0315           					 # Rayon roue du robot
nbr_puls_roue = 410.189			# Nombre pulsation pour faire un tour de robot sur lui-meme

def avancer_de(mm):
	while True:
		if __name__ == '__main__':
	
			try:
				listener()
			except:
				pass
		else continue


def reculer_de(mm):
	pass

def tourner_de(deg):
	pass

def pause_de(s):
	pass

def stop():
	pass



def callback_encoders(msg):
	return msg


def listener():
	
	rospy.Subscriber('pub_encoders', Encoders, callback_encoders(test))
	
	rospy.spin()


if __name__ == '__main__':
	
	try:
		listener()
	except:
		pass
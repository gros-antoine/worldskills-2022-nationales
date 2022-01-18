import rospy
from std_msgs.msg import String, Float32MultiArray
from scipy.spatial import distance as dist
from collections import OrderedDict
import cv2
import imutils
import numpy as np
import color_labeler

pub_ok = rospy.Publisher('pub_ok', String, queue_size=10)
pub_avancer = rospy.Publisher('pub_avancer', Float32MultiArray, queue_size=10)
pub_tournerd = rospy.Publisher('pub_tournerd', String, queue_size=10)
pub_tournerg = rospy.Publisher('pub_tournerg', String, queue_size=10)
pub_verifangle = rospy.Publisher('pub_verifangle', String, queue_size=10)
pub_reculer = rospy.Publisher('pub_reculer', String, queue_size=10)

class ColorLabeler:

	def __init__(self):

		# A MODIFIER SELON LES MEILLEURS COULEURS SUR PISTE
		colors = OrderedDict({
			"red": (150, 25, 45),
			"green": (0, 104, 40),
			"blue": (0, 28, 108),
			"yellow": (115, 137, 6)})

		self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
		self.colorNames = []

		for (i, (name, rgb)) in enumerate(colors.items()):
			self.lab[i] = rgb
			self.colorNames.append(name)

		self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)

	def label(self, image, c):

		# Construit un masque pour le contour et calcule ensuite
		# la couleur moyenne L*a*b pour la zone dans le masque
		mask = np.zeros(image.shape[:2], dtype="uint8")
		cv2.drawContours(mask, [c], -1, 255, -1)
		mask = cv2.erode(mask, None, iterations=2)
		mean = cv2.mean(image, mask=mask)[:3]

		# Initie la distance minimum
		minDist = (np.inf, None)

		for (i, row) in enumerate(self.lab):

			# Calcule la distace entre la couleur L*a*b* actuelle
			# et la couleur moyenne de la région
			d = dist.euclidean(row[0], mean)

			# Si la distance est plus petite que la distance actuelle
			# on l'update
			if d < minDist[0]:
				minDist = (d, i)

		return self.colorNames[minDist[1]]


color = ""

def take_image():

	# Ouvre le flux video
	vid = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)

	# Definit la taille de l'image
	vid.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)
	vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)

	# Lis le flux et converti en RGB
	_, img = vid.read()
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	vid.release()

	return img


def callback(data):

	global color

	if(data.data == "1"):

		colorLabeler = ColorLabeler()

		#image = cv2.imread('image7.jpg')
		image = take_image()
		print("image prise")
		cv2.waitKey(0)
		resized = imutils.resize(image, width=300)
		ratio = image.shape[0] / float(resized.shape[0])

		# On floute l'image
		blurred = cv2.GaussianBlur(resized, (5, 5), 0)
		gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
		lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
		thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)[1]

		# Definie une matrice 5x5 d'entier (?)  
		kernel = np.ones((7,7),np.uint8)

		# Enleve le bruit sur le noir du masque
		thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
		# Enleve le bruit sur le blanc du masque
		thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

		'''for i in range(len(thresh)):
			for j in range(len(thresh[0])):
				thresh[i][j] = 255 - thresh[i][j]'''

		# Inversion image finie
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)

		color = ''

		for c in cnts:

			#cv2.drawContours(blurred, [c], -1, (0, 255, 0), 2)

			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.04 * peri, True)
			print(approx)
			if(len(approx) <= 6):
				continue
			else:
				color = colorLabeler.label(lab, c)

		if(color == ""):

			lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

			hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

			lower_bound = np.array([26, 170, 50])   
			upper_bound = np.array([66, 255, 255])

			# Creation d'un masque qui ne garde que les pixels qui sont dans la plage definie
			mask = cv2.inRange(hsv, lower_bound, upper_bound)

			# Definie une matrice 5x5 d'entier (?)  
			kernel = np.ones((7,7),np.uint8)

			# Enleve le bruit sur le noir du masque
			mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
			# Enleve le bruit sur le blanc du masque
			mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

			cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			cnts = imutils.grab_contours(cnts)

			for c in cnts:

				peri = cv2.arcLength(c, True)
				approx = cv2.approxPolyDP(c, 0.04 * peri, True)

				if(len(approx) > 5):
					color = colorLabeler.label(lab, c)

		pub_ok.publish("ok")

	if(data.data == "2"):

		msg = Float32MultiArray()

		if(color == "yellow"):
			msg.data = [0, 90]
			pub_avancer.publish(msg)
		elif(color == "green"):
			msg.data = [300, 90]
			pub_avancer.publish(msg)
		elif(color == "blue"):
			msg.data = [600, 90]
			pub_avancer.publish(msg)
		elif(color == "red"):
			msg.data = [900, 90]
			pub_avancer.publish(msg)

	if(data.data == "3"):

		msg = Float32MultiArray()

		if(color == "yellow"):
			msg.data = [1400, -270]
			pub_avancer.publish(msg)
		elif(color == "green"):
			msg.data = [1400 - 300, -270]
			pub_avancer.publish(msg)
		elif(color == "blue"):
			msg.data = [1400 - 600, -270]
			pub_avancer.publish(msg)
		elif(color == "red"):
			msg.data = [1400 - 900, -270]
			pub_avancer.publish(msg)

	if(data.data == "4"):

		msg = Float32MultiArray()

		if(color == "blue"):
			msg.data = [0, -180]
			pub_avancer.publish(msg)

		elif(color == "green"):
			msg.data = [300, -180]
			pub_avancer.publish(msg)

		elif(color == "yellow"):
			msdata = [300+290, -180]
			pub_avancer.publish(msg)

		elif(color == "red"):
			msg.data = [300+290, -180]
			pub_avancer.publish(msg)

	if(data.data == "5"):

		msg = String()

		if(color == "red"):
			msg.data = "90"
			pub_tournerd.publish(msg)
		else:
			msg.data = "0"
			pub_tournerd.publish(msg)

	if(data.data == "6"):

		msg = Float32MultiArray()

		if(color == "red"):
			msg.data = [300, -270]
			pub_avancer.publish(msg)
		else:
			msg.data = [0, -270]
			pub_avancer.publish(msg)

	if(data.data == "7"):

		msg = String()
		
		if(color == "red"):
			msg.data = "-630"
			pub_verifangle.publish(msg)
		else:
			msg.data = "-540"
			pub_verifangle.publish(msg)

	if(data.data == "8"):

		msg = String()

		if(color == "red"):
			msg.data = "300"
			pub_reculer.publish(msg)
		else:
			msg.data = "0"
			pub_reculer.publish(msg)

	if(data.data == "9"):

		msg = String()
		if(color == "red"):
			msg.data = "90"
			pub_tournerg.publish(msg)
		else:
			msg.data = "0"
			pub_tournerg.publish(msg)

	
def listener():
	rospy.init_node('programme_camera')
	rospy.Subscriber("pub_camera", String, callback)
	rospy.spin()


if __name__ == '__main__':
	try:
		listener()
	except:
			pass
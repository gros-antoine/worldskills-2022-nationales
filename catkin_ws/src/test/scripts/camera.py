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
pub_verifdistance = rospy.Publisher('pub_verifdistance', String, queue_size=10)

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


color1 = ""

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

	global color1
	global color2
	global color3

	if(data.data == "1"):

		colorLabeler = ColorLabeler()

		#image = cv2.imread('image7.jpg')
		image = take_image()
		cv2.waitKey(0)
		resized = imutils.resize(image, width=300)
		ratio = image.shape[0] / float(resized.shape[0])

		# On floute l'image
		blurred = cv2.GaussianBlur(resized, (5, 5), 0)
		gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
		lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
		thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)[1]

		cv2.imwrite("thresh.jpg", thresh)

		# Definie une matrice 5x5 d'entier (?)  
		kernel = np.ones((7,7),np.uint8)

		# Enleve le bruit sur le noir du masque
		thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
		# Enleve le bruit sur le blanc du masque
		thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

		# Inversion image finie
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)

		color1 = ''

		for c in cnts:

			#cv2.drawContours(blurred, [c], -1, (0, 255, 0), 2)
			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.04 * peri, True)
			if(len(approx) <= 6):
				continue
			else:
				color1 = colorLabeler.label(lab, c)

		if(color1 == ""):

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
					color1 = colorLabeler.label(lab, c)

		if(color1 == ""):
			color1 = "blue"

		pub_ok.publish("ok")

	elif(data.data == "2"):

		colorLabeler = ColorLabeler()

		#image = cv2.imread('image7.jpg')
		image = take_image()
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

		# Inversion image finie
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)

		color2 = ''

		for c in cnts:

			#cv2.drawContours(blurred, [c], -1, (0, 255, 0), 2)

			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.04 * peri, True)
			if(len(approx) <= 6):
				continue
			else:
				color2 = colorLabeler.label(lab, c)

		if(color2 == ""):

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
					color2 = colorLabeler.label(lab, c)

		if(color2 == ""):
			color2 = "blue"

		pub_ok.publish("ok")

	elif(data.data == "3"):

		colorLabeler = ColorLabeler()

		#image = cv2.imread('image7.jpg')
		image = take_image()
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

		# Inversion image finie
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)

		color3 = ''

		for c in cnts:

			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.04 * peri, True)
			if(len(approx) <= 6):
				continue
			else:
				color3 = colorLabeler.label(lab, c)

		if(color3 == ""):

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
					color3 = colorLabeler.label(lab, c)

		pub_ok.publish("ok")

		if(color3 == ""):
			color3 = "blue"

	
	elif(data.data == "4"):

		msg = Float32MultiArray()

		if(color1 == "blue"):
			pub_ok.publish("ok")
		elif(color1 == "green"):
			msg.data = [300, -180]
			pub_avancer.publish(msg)
		elif(color1 == "yellow" or color1 == "red"):
			msg.data = [300+290, -180]
			pub_avancer.publish(msg)

	# Verif distance fond
	elif(data.data == "5"):

		msg = String()

		if(color1 == "red" or color1 == "yellow"):
			msg.data = "20.5"
			pub_verifdistance.publish(msg)
		else:
			pub_ok.publish("ok")

	# Tourner 90 pour le rouge
	elif(data.data == "6"):

		msg = String()

		if(color1 == "red"):
			msg.data = "90"
			pub_tournerd.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif angle rouge
	elif(data.data == "7"):

		msg = String()

		if(color1 == "red"):
			msg.data = "-270"
			pub_verifangle.publish(msg)
		else:
			pub_ok.publish("ok")

	# Avancer jusqu'à rouge
	elif(data.data == "8"):

		msg = Float32MultiArray()

		if(color1 == "red"):
			msg.data = [295, -270]   # A verifier par rapport à la verif dist précédente
			pub_avancer.publish(msg)
		else:
			pub_ok.publish("ok")


	# Verif distance rouge
	elif(data.data == "9"):

		msg = String()

		if(color1 == "red"):
			msg.data = "14.5"
			pub_verifdistance.publish(msg)
		else:
			pub_ok.publish("ok")

	# tour sur nous meme
	elif(data.data == "10"):

		msg = String()

		msg.data = "360"
		pub_tournerg.publish(msg)

	# Verif angle
	elif(data.data == "11"):

		msg = String()

		if(color1 == "red"):
			msg.data = "90"
			pub_verifangle.publish(msg)
		else:
			msg.data = "180"
			pub_verifangle.publish(msg)

	# Demi tour rouge
	elif(data.data == "12"):

		msg = String()

		if(color1 == "red"):
			msg.data = "180"
			pub_tournerg.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif angle apres demi tour rouge
	elif(data.data == "13"):

		msg = String()

		if(color1 == "red"):
			msg.data = "270"
			pub_verifangle.publish(msg)
		else:
			pub_ok.publish("ok")

	# retour du rouge sur le jaune
	elif(data.data == "14"):

		msg = Float32MultiArray()

		if(color1 == "red"):
			msg.data = [295, 270]  # A verif sur run (295)
			pub_avancer.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif distance rouge
	elif(data.data == "15"):

		msg = String()

		if(color1 == "red"):
			msg.data = "14"
			pub_verifdistance.publish(msg)
		else:
			pub_ok.publish("ok")


	# 90° pour s'aligner si rouge
	elif(data.data == "16"):

		msg = String()

		if(color1 == "red"):
			msg.data = "90"
			pub_tournerd.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif angle apres demi tour rouge
	elif(data.data == "17"):

		msg = String()

		if(color1 == "red"):
			msg.data = "180"
			pub_verifangle.publish(msg)
		else:
			pub_ok.publish("ok")

	# tous demi tour, les mets à un angle de 0
	elif(data.data == "18"):

		msg = String()

		msg.data = "180"
		pub_tournerd.publish(msg)


	# Verif apres demi tour
	elif(data.data == "19"):

		msg = String()

		msg.data = "0"
		pub_verifangle.publish(msg)

	# Avancer jusqu'à bleu
	elif(data.data == "20"):

		msg = Float32MultiArray()

		if(color1 == "blue"):
			pub_ok.publish("ok")
		elif(color1 == "green"):
			msg.data = [300, 0]
			pub_avancer.publish(msg)
		elif(color1 == "yellow" or color1 == "red"):
			msg.data = [300+290, 0]
			pub_avancer.publish(msg)

	# Verif distance en face sur le bleu
	elif(data.data == "21"):

		msg = String()
		msg.data = "18.75"
		pub_verifdistance.publish(msg)

	# 90 pour aligner mur gauche
	elif(data.data == "22"):

		msg = String()

		msg.data = "90"
		pub_tournerd.publish(msg)

	# Verif apres demi tour
	elif(data.data == "23"):

		msg = String()

		msg.data = "-90"
		pub_verifangle.publish(msg)


	# Verif distance a gauche
	elif(data.data == "24"):

		msg = String()

		msg.data = "14"
		pub_verifdistance.publish(msg)

	# 90 pour s'aligner position initiale
	elif(data.data == "25"):

		msg = String()

		msg.data = "90"
		pub_tournerd.publish(msg)

	# Verif apres demi tour
	elif(data.data == "26"):

		msg = String()

		msg.data = "-180"
		pub_verifangle.publish(msg)


	elif(data.data == "27"):

		msg = Float32MultiArray()

		if(color2 == "blue"):
			pub_ok.publish("ok")
		elif(color2 == "green"):
			msg.data = [300, -180]
			pub_avancer.publish(msg)
		elif(color2 == "yellow" or color2 == "red"):
			msg.data = [300+290, -180]
			pub_avancer.publish(msg)

	# Verif distance fond
	elif(data.data == "28"):

		msg = String()

		if(color2 == "red" or color2 == "yellow"):
			msg.data = "20.5"
			pub_verifdistance.publish(msg)
		else:
			pub_ok.publish("ok")

	# Tourner 90 pour le rouge
	elif(data.data == "29"):

		msg = String()

		if(color2 == "red"):
			msg.data = "90"
			pub_tournerd.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif angle rouge
	elif(data.data == "30"):

		msg = String()

		if(color2 == "red"):
			msg.data = "-270"
			pub_verifangle.publish(msg)
		else:
			pub_ok.publish("ok")

	# Avancer jusqu'à rouge
	elif(data.data == "31"):

		msg = Float32MultiArray()

		if(color2 == "red"):
			msg.data = [295, -270]   # A verifier par rapport à la verif dist précédente
			pub_avancer.publish(msg)
		else:
			pub_ok.publish("ok")


	# Verif distance rouge
	elif(data.data == "32"):

		msg = String()

		if(color2 == "red"):
			msg.data = "14.5"
			pub_verifdistance.publish(msg)
		else:
			pub_ok.publish("ok")

	# tour sur nous meme
	elif(data.data == "33"):

		msg = String()

		msg.data = "360"
		pub_tournerg.publish(msg)

	# Verif angle
	elif(data.data == "34"):

		msg = String()

		if(color2 == "red"):
			msg.data = "90"
			pub_verifangle.publish(msg)
		else:
			msg.data = "180"
			pub_verifangle.publish(msg)

	# Demi tour rouge
	elif(data.data == "35"):

		msg = String()

		if(color2 == "red"):
			msg.data = "180"
			pub_tournerg.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif angle apres demi tour rouge
	elif(data.data == "36"):

		msg = String()

		if(color2 == "red"):
			msg.data = "270"
			pub_verifangle.publish(msg)
		else:
			pub_ok.publish("ok")

	# retour du rouge sur le jaune
	elif(data.data == "37"):

		msg = Float32MultiArray()

		if(color2 == "red"):
			msg.data = [295, 270]  # A verif sur run (295)
			pub_avancer.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif distance rouge
	elif(data.data == "38"):

		msg = String()

		if(color2 == "red"):
			msg.data = "14"
			pub_verifdistance.publish(msg)
		else:
			pub_ok.publish("ok")


	# 90° pour s'aligner si rouge
	elif(data.data == "39"):

		msg = String()

		if(color2 == "red"):
			msg.data = "90"
			pub_tournerd.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif angle apres demi tour rouge
	elif(data.data == "40"):

		msg = String()

		if(color2 == "red"):
			msg.data = "180"
			pub_verifangle.publish(msg)
		else:
			pub_ok.publish("ok")

	# tous demi tour, les mets à un angle de 0
	elif(data.data == "41"):

		msg = String()

		msg.data = "180"
		pub_tournerd.publish(msg)


	# Verif apres demi tour
	elif(data.data == "42"):

		msg = String()

		msg.data = "0"
		pub_verifangle.publish(msg)

	# Avancer jusqu'à bleu
	elif(data.data == "43"):

		msg = Float32MultiArray()

		if(color2 == "blue"):
			pub_ok.publish("ok")
		elif(color2 == "green"):
			msg.data = [300, 0]
			pub_avancer.publish(msg)
		elif(color2 == "yellow" or color2 == "red"):
			msg.data = [300+290, 0]
			pub_avancer.publish(msg)

	# Verif distance en face sur le bleu
	elif(data.data == "44"):

		msg = String()
		msg.data = "18.75"
		pub_verifdistance.publish(msg)

	# 90 pour aligner mur gauche
	elif(data.data == "45"):

		msg = String()

		msg.data = "90"
		pub_tournerd.publish(msg)

	# Verif apres demi tour
	elif(data.data == "46"):

		msg = String()

		msg.data = "-90"
		pub_verifangle.publish(msg)


	# Verif distance a gauche
	elif(data.data == "47"):

		msg = String()

		msg.data = "14"
		pub_verifdistance.publish(msg)

	# 90 pour s'aligner position initiale
	elif(data.data == "48"):

		msg = String()

		msg.data = "90"
		pub_tournerd.publish(msg)

	# Verif apres demi tour
	elif(data.data == "49"):

		msg = String()

		msg.data = "-180"
		pub_verifangle.publish(msg)


	elif(data.data == "50"):

		msg = Float32MultiArray()

		if(color3 == "blue"):
			pub_ok.publish("ok")
		elif(color3 == "green"):
			msg.data = [300, -180]
			pub_avancer.publish(msg)
		elif(color3 == "yellow" or color3 == "red"):
			msg.data = [300+290, -180]
			pub_avancer.publish(msg)

	# Verif distance fond
	elif(data.data == "51"):

		msg = String()

		if(color3 == "red" or color3 == "yellow"):
			msg.data = "20.5"
			pub_verifdistance.publish(msg)
		else:
			pub_ok.publish("ok")

	# Tourner 90 pour le rouge
	elif(data.data == "52"):

		msg = String()

		if(color3 == "red"):
			msg.data = "90"
			pub_tournerd.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif angle rouge
	elif(data.data == "53"):

		msg = String()

		if(color3 == "red"):
			msg.data = "-270"
			pub_verifangle.publish(msg)
		else:
			pub_ok.publish("ok")

	# Avancer jusqu'à rouge
	elif(data.data == "54"):

		msg = Float32MultiArray()

		if(color3 == "red"):
			msg.data = [295, -270]   # A verifier par rapport à la verif dist précédente
			pub_avancer.publish(msg)
		else:
			pub_ok.publish("ok")


	# Verif distance rouge
	elif(data.data == "55"):

		msg = String()

		if(color3 == "red"):
			msg.data = "14.5"
			pub_verifdistance.publish(msg)
		else:
			pub_ok.publish("ok")

	# tour sur nous meme
	elif(data.data == "56"):

		msg = String()

		msg.data = "360"
		pub_tournerg.publish(msg)

	# Verif angle
	elif(data.data == "57"):

		msg = String()

		if(color3 == "red"):
			msg.data = "90"
			pub_verifangle.publish(msg)
		else:
			msg.data = "180"
			pub_verifangle.publish(msg)

	# Demi tour rouge
	elif(data.data == "58"):

		msg = String()

		if(color3 == "red"):
			msg.data = "180"
			pub_tournerg.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif angle apres demi tour rouge
	elif(data.data == "59"):

		msg = String()

		if(color3 == "red"):
			msg.data = "270"
			pub_verifangle.publish(msg)
		else:
			pub_ok.publish("ok")

	# retour du rouge sur le jaune
	elif(data.data == "60"):

		msg = Float32MultiArray()

		if(color3 == "red"):
			msg.data = [295, 270]  # A verif sur run (295)
			pub_avancer.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif distance rouge
	elif(data.data == "61"):

		msg = String()

		if(color3 == "red"):
			msg.data = "14"
			pub_verifdistance.publish(msg)
		else:
			pub_ok.publish("ok")


	# 90° pour s'aligner si rouge
	elif(data.data == "62"):

		msg = String()

		if(color3 == "red"):
			msg.data = "90"
			pub_tournerd.publish(msg)
		else:
			pub_ok.publish("ok")

	# Verif angle apres demi tour rouge
	elif(data.data == "63"):

		msg = String()

		if(color3 == "red"):
			msg.data = "180"
			pub_verifangle.publish(msg)
		else:
			pub_ok.publish("ok")

	# tous demi tour, les mets à un angle de 0
	elif(data.data == "64"):

		msg = String()

		msg.data = "180"
		pub_tournerd.publish(msg)


	# Verif apres demi tour
	elif(data.data == "65"):

		msg = String()

		msg.data = "0"
		pub_verifangle.publish(msg)

	# Avancer jusqu'à bleu
	elif(data.data == "66"):

		msg = Float32MultiArray()

		if(color3 == "blue"):
			pub_ok.publish("ok")
		elif(color3 == "green"):
			msg.data = [300, 0]
			pub_avancer.publish(msg)
		elif(color3 == "yellow" or color3 == "red"):
			msg.data = [300+290, 0]
			pub_avancer.publish(msg)

	# Verif distance en face sur le bleu
	elif(data.data == "67"):

		msg = String()
		msg.data = "18.75"
		pub_verifdistance.publish(msg)

	# 90 pour aligner mur gauche
	elif(data.data == "68"):

		msg = String()

		msg.data = "90"
		pub_tournerd.publish(msg)

	# Verif apres demi tour
	elif(data.data == "69"):

		msg = String()

		msg.data = "-90"
		pub_verifangle.publish(msg)


	# Verif distance a gauche
	elif(data.data == "70"):

		msg = String()

		msg.data = "14"
		pub_verifdistance.publish(msg)

	# 90 pour s'aligner position initiale
	elif(data.data == "71"):

		msg = String()

		msg.data = "90"
		pub_tournerd.publish(msg)

	# Verif apres demi tour
	elif(data.data == "72"):

		msg = String()

		msg.data = "-180"
		pub_verifangle.publish(msg)










	'''if(data.data == "2"):

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
			msg.data = [250, -270]
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
			msg.data = "250"
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

	if(data.data == "10"):

		msg = Float32MultiArray()
		if(color == "red" or color == "yellow"):
			msg.data = [290+300-50, -720]
			pub_avancer.publish(msg)
		elif(color == "green"):
			msg.data = [300-50, -720]
			pub_avancer.publish(msg)
		elif(color == "blue"):
			msg.data = [0, -720]
			pub_avancer.publish(msg)'''

	
def listener():
	rospy.init_node('programme_camera')
	rospy.Subscriber("pub_camera", String, callback)
	rospy.spin()


if __name__ == '__main__':
	try:
		listener()
	except:
			pass
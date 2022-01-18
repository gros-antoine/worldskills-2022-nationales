from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2

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
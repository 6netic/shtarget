import cv2
import numpy as np


class Extract:
	""" this class extracts main form from image """


	def __init__(self, img, imgThresh):
				
		self.img = img
		self.imgThresh = imgThresh


	def sumOfAllProcesses(self):
		""" This function extracts the target from the background """

		# Get the contours
		copy1Img = self.img.copy()
		contours, hierarchy = cv2.findContours(self.imgThresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		contours_list = []
		for contour in range(len(contours)):
			contours_list.append(cv2.contourArea(contours[contour]))
		# selected_contour is the biggest contour found
		max_selected_contour_index = contours_list.index(max(contours_list))
		selected_contour = contours[max_selected_contour_index]
		# Get Shape of the biggest contour
		copy2Img = self.img.copy()
		perimeter = cv2.arcLength(selected_contour,True)
		approx = cv2.approxPolyDP(selected_contour, 0.02 * perimeter, True)		
		# Rearrange the 4 coordinates
		newCoords = np.zeros_like(approx)
		coords = approx.reshape((4, 2))
		addition = coords.sum(1)
		newCoords[0] = coords[np.argmin(addition)]
		newCoords[3] = coords[np.argmax(addition)]
		difference = np.diff(coords, axis=1)
		newCoords[1] = coords[np.argmin(difference)]
		newCoords[2] = coords[np.argmax(difference)]		
		# Generate new target image only
		copy3 = self.img.copy()
		width, height = 799, 799
		coords1 = np.float32(newCoords)
		coords2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
		matrix = cv2.getPerspectiveTransform(coords1, coords2)
		extractImg = cv2.warpPerspective(copy3, matrix, (width, height))

		return extractImg
		
		



















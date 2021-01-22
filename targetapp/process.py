import cv2
import numpy as np


class Process:
	""" This class processes the image and applies some filters """


	def __init__(self, img):
		
		self.img = img
		
	
	def sumOfAllProcesses(self):
		""" Transforms the RGB image into binary image """

		# Adding color intensity
		M1 = np.ones(self.img.shape, dtype="uint8") * 20
		addImg = cv2.add(self.img, M1)
		# Converting to gray image
		grayImg = cv2.cvtColor(addImg, cv2.COLOR_BGR2GRAY)
		# Applying Gaussian blur filter
		blurImg = cv2.GaussianBlur(grayImg, (3, 3), 1)
		# Applying Canny filter
		cannyImg = cv2.Canny(blurImg, 40, 70)
		# Applying Dilate filter
		kernel1 = np.ones((3, 3), np.uint8)
		dilateImg = cv2.dilate(cannyImg, kernel1, iterations=2)
		# Applying Erode filter
		kernel2 = np.ones((3, 3), np.uint8)
		erodeImg = cv2.erode(dilateImg, kernel2, iterations=1)
		
		return erodeImg














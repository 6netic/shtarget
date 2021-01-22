
from ..extract import *


def test_image_extract():
	""" Testing if image can be extracted from background """

	img1 = "targetapp/tests/img_ok_test.jpeg"	
	img1Temp = open(img1, "rb").read()
	image1_array = np.asarray(bytearray(img1Temp), dtype=np.uint8)
	img1_opencv = cv2.imdecode(image1_array, -1)
	
	img2 = "targetapp/tests/img_ok_processImg_test.jpg"
	img2Temp = open(img2, "rb").read()
	image2_array = np.asarray(bytearray(img2Temp), dtype=np.uint8)
	img2_opencv = cv2.imdecode(image2_array, -1)

	extractImg = Extract(img1_opencv, img2_opencv)
	extractImg = extractImg.sumOfAllProcesses()

	response = isinstance(extractImg.shape, tuple)
	assert response == True
	assert extractImg.shape == (799, 799, 3)


	

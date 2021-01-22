from ..process import *


# load a random image
def test_image_process():
	""" Testing if image can be processed in first step correctly """

	# We open the file to work with it - I'm taking what is in views file.
	img = "targetapp/tests/img_ok_test.jpeg"
	imgTemp = open(img, "rb").read()
	image_array = np.asarray(bytearray(imgTemp), dtype=np.uint8)
	img_opencv = cv2.imdecode(image_array, -1)

	imgTreatment = Process(img_opencv)
	imgTreatment = imgTreatment.sumOfAllProcesses()
	
	response = isinstance(imgTreatment.shape, tuple)	
	number = len(imgTreatment.shape)
	# We check if response represents a tuple
	assert response == True
	# We check if response represents a grayscale image
	assert number == 2





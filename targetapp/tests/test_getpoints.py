
from ..getpoints import *


def test_image_getPoints():
	""" Testing if image can be extracted from background """

	img1 = "targetapp/tests/img_ok_extractImg_test.jpg"	
	img1Temp = open(img1, "rb").read()
	image1_array = np.asarray(bytearray(img1Temp), dtype=np.uint8)
	img_opencv = cv2.imdecode(image1_array, -1)

	getPoints = CountPoints(img_opencv)
	resp = getPoints.getBiggestCircleRadius(img_opencv, (3, 3), [40, 70], (3, 3))
	response = isinstance(resp, dict)
	assert response == True
	assert len(resp) == 4

	contourImg, x_centroid, y_centroid, radiusCircle = \
				resp["cntImg"], resp["xCenter"], resp["yCenter"], resp["radius"]			
	holesImg = getPoints.getHoles(x_centroid, y_centroid, radiusCircle)
	assert holesImg.shape == (799, 799, 3)


	
	

from targetapp import app


def test_index_page_get():
	""" This function tests the GET method for 'index' route """

	response = app.test_client().get('/')
	assert response.status_code == 200
	assert b'css/styles.css' in response.data	
	assert b'<input type="file" name="srcfile" id="srcfile" accept="image/*">' in response.data
	assert b'<button type="submit">Calcul des points</button>'


def test_index_view_with_post_upload_image_is_200():
	""" Testing if code 200 is returned when file is Ok with POST method on 'index' route """

	url = '/'
	data = { 'srcfile': (open("targetapp/tests/img_ok_test.jpeg", "rb"), "img_ok_test.jpeg") }
	response = app.test_client().post(
				url,
				buffered = True,
				follow_redirects = True,
				content_type = 'multipart/form-data',
				data = data
			)
	assert response.status_code == 200


def test_index_view_with_post_upload_image_is_500():
	""" Testing if code 500 is returned when no file is selected 
	with POST method on 'index' route """

	url = '/'
	data = { 'srcfile' : (open("targetapp/tests/img_ok_test.jpeg", "rb"), "")}
	response = app.test_client().post(
				url,
				buffered = True,
				follow_redirects = True,
				content_type = 'multipart/form-data',
				data = data
			)
	assert response.status_code == 500


def test_index_view_with_post_upload_image_is_400():
	""" Testing if code 400 is returned when file extension is not allowed """

	url = '/'
	data = { 'srcfile' : (open("targetapp/tests/img_error_test.txt", "rb"), "img_error_test.txt")}
	response = app.test_client().post(
				url,
				buffered = True,
				follow_redirects = True,
				content_type = 'multipart/form-data',
				data = data
			)
	assert response.status_code == 400


def test_index_view_with_post_upload_image_is_not_413():
	""" Testing if code 413 is returned when no file size is too big """

	url = '/'
	data = { 'srcfile' : (open("targetapp/tests/img_ok_test.jpeg", "rb"), "img_ok_test.jpeg")}
	response = app.test_client().post(
				url,
				buffered = True,
				follow_redirects = True,
				content_type = 'multipart/form-data',
				data = data
			)
	assert response.status_code != 413


def test_index_view_with_post_upload_image_is_409():
	""" Testing if code 409 is returned when image cannot be treated as expected """

	url = '/'
	data = { 'srcfile' : (open("targetapp/tests/img_error_test.jpeg", "rb"), "img_error_test.jpeg")}
	response = app.test_client().post(
				url,
				buffered = True,
				follow_redirects = True,
				content_type = 'multipart/form-data',
				data = data
			)
	assert response.status_code == 409





import os
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
import cv2
import numpy as np
from .process import *
from .extract import *
from .getpoints import *


app = Flask(__name__)

IMG_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['ALLOWED_EXTENSIONS'] = ["jpeg", "jpg", "png"]
app.config['UPLOAD_FOLDER'] = os.path.join(IMG_DIR, 'static', 'in')
app.config['OUTPUT_FOLDER'] = os.path.join(IMG_DIR, 'static', 'out')

@app.route("/", methods=['GET', 'POST'])
def index():
	
	# POST request
	if request.method == "POST":
		if request.files:
			image = request.files['srcfile']
			# Check if file is empty
			if image.filename == "":
				data = { "mess" : "Vous devez sélectionner un fichier contenant une image !" }
				return jsonify(data), 500
			# Check if file extension is allowed
			if image.filename.rsplit('.', 1)[1].lower() not in app.config['ALLOWED_EXTENSIONS']:
				data = { "mess" : "Seules les extensions jpg, jpeg et png sont autorisées !" }
				return jsonify(data), 400
			# Securing and saving file to the disk
			filename = secure_filename(image.filename)
			image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			# Checking file size
			if (os.stat(img).st_size) > 3000000:
				os.remove(img)
				data = { "mess" : "La taille du fichier ne doit pas excéder 3 Mo !" }
				return jsonify(data), 413

			# We open and decode the file to work with it
			imgTemp = open(img, "rb").read()
			image_array = np.asarray(bytearray(imgTemp), dtype=np.uint8)
			img_opencv = cv2.imdecode(image_array, -1)
			# Processing the image
			processImg = Process(img_opencv)
			processImg = processImg.sumOfAllProcesses()
			# Extracting the image
			extractImg = Extract(img_opencv, processImg)
			try:
				extractImg = extractImg.sumOfAllProcesses()
			except ValueError:
				os.remove(img)
				data = { "mess" : "Echec. La couleur du fond n'a pas pu être dissociée." }
				return jsonify(data), 409
			# Getting biggest circle and holes from the target
			getPoints = CountPoints(extractImg)
			try:
				resp = getPoints.getBiggestCircleRadius(extractImg, (3, 3), [40, 70], (3, 3))
				contourImg, x_centroid, y_centroid, radiusCircle = \
						resp["cntImg"], resp["xCenter"], resp["yCenter"], resp["radius"]			
				holesImg = getPoints.getHoles(x_centroid, y_centroid, radiusCircle)
			except:
				os.remove(img)
				data = { "mess" : "Echec. Impossible de repérer les 10 trous." }
				return jsonify(data), 409
						
			# Saving the image
			tempFile = os.path.join(app.config['OUTPUT_FOLDER'], 'temp.jpg')
			cv2.imwrite(tempFile, holesImg) #holesImg
			os.remove(img)
			dateNow = datetime.now().strftime('%Y%m%d%H%M%S')
			data = dateNow
			return jsonify(data), 200		

	else:
		# GET request
		return render_template("index.html")
	





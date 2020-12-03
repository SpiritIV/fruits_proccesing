# USAGE
# Start the server:
# 	python run_front_server.py
# Submit a request via Python:
#	python simple_request.py

# import the necessary packages
from keras.models import load_model
import pandas as pd
import numpy as np
from keras.preprocessing.image import img_to_array, load_img
import os

#import cloudpickle
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime

# initialize our Flask application and the model
app = flask.Flask(__name__)
model = None

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def load_model(model_path):
	# load the pre-trained model
	global fruit_model
	with open(model_path, 'rb') as f:
		fruit_model = load_model(model_path)

modelpath = "/app/models"
load_model(modelpath)

@app.route("/", methods=["GET"])
def general():
	return """Welcome to fruit's prediction process. Please use 'http://<address>/predict' to POST"""

@app.route("/predict", methods=["POST"])
def predict():
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}
	dt = strftime("[%Y-%b-%d %H:%M:%S]")
	# ensure an image was properly uploaded to our endpoint
	if flask.request.method == "POST":

		request_json = flask.request.get_json()
		path = request_json['path']
		img = load_img(path, target_size=(100, 100))
		images_as_array = []
		images_as_array.append(img_to_array(img))
		X_img = np.array(images_as_array)
		try:
			classes = ['Banana', 'Cocos', 'Mandarine', 'Orange', 'Peach', 'Pineapple', 'Strawberry']
			preds = fruit_model.predict(X_img)
			preds = preds[0]
			preds = classes[[preds].argmax(axis=0)]
		except AttributeError as e:
			logger.warning(f'{dt} Exception: {str(e)}')
			data['predictions'] = str(e)
			data['success'] = False
			return flask.jsonify(data)

		data["predictions"] = preds
		# indicate that the request was a success
		data["success"] = True

	# return the data dictionary as a JSON response
	return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading the model and Flask starting server..."
		"please wait until server has fully started"))
	port = int(os.environ.get('PORT', 8180))
	app.run(host='0.0.0.0', debug=True, port=port)

import sys
sys.path.append("..")

import os
import time
import random

from flask import Flask, json, flash, Response, request, render_template, redirect, url_for 
from werkzeug.utils import secure_filename
from tclustering import fsp


app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "templates"))
app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), "uploads")

@app.route('/')
def root():
	return render_template("index.html")

@app.route('/upload', methods=['GET','POST'])
def uploadXES():
	if request.method == "POST":
		if 'file' not in request.files:
			return json_error("No file in request")
		file = request.files['file']
		if file.filename == '':
			return json_error("No selected file")
		if file and check_file_type(file.filename):
			filename = str(int(round(time.time() * 1000))) + "-" +  str(random.randint(100,999)) + ".xes"
			fpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(fpath)
			first = fsp.FSP(fpath ,0.8)
			return ""


def run_server(p_debug=False):
	app.run(debug=p_debug)

def json_error(msg):
	#Returns error message to user in JSON format
	return json_response({"status": "error", "message": msg});

def json_response(rsp):
	#Changes response type from HTML to JSON
	return app.response_class(response=json.dumps(rsp), mimetype="application/json")

def check_file_type(filename):
	#Checks file type, XES is currently the only one that's allowed
	return filename.lower().endswith(('.xes'))
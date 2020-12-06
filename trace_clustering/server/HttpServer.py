import sys

import os
import time
import random

from flask import Flask, session, json, flash, Response, request, render_template, redirect, url_for 
from werkzeug.utils import secure_filename
from tclustering import cluster as c

sys.path.append("..")

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "templates"))
app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), "uploads")
app.secret_key = 'Abraham Lincoln was the president of the United States'


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
			#algo, params, label, file_path
			#cluster= c.Cluster([0], ["Activity","Resource"], fpath)
			session["xes"] = fpath
			return redirect('select')



@app.route('/sample', methods=['GET','POST'])
def sample():
	if session_isset("xes"):
		if (
			request.method == "POST"
			and form_isset("selected")
			and form_isset("thresholds")
			and form_isset("labels")
		):
			session["selected"] = json.loads(request.form.get("selected"))
			session["thresholds"] = json.loads(request.form.get("thresholds"))
			print(session["thresholds"] );
			session["labels"] = json.loads(request.form.get("labels"))
			return redirect('result')
		return render_template('sample.html')
	return redirect("error")


@app.route('/select', methods=['GET','POST'])
def select():
	return render_template('select.html')


@app.route('/result', methods=['GET','POST'])
def result():
	if (
		session_isset("selected")
		and session_isset("thresholds")
		and session_isset("labels")
		and session_isset("xes")
	):
		fsp1 = c.Cluster(session["xes"], session["selected"], session["labels"], 0.8, ["CloFast", "SPAM", "SPAM"], session["thresholds"])
		return json_response(fsp1.clustering);
	return redirect("error")


@app.route('/error')
def error():
	return render_template("error.html")


@app.route('/table/json')
def tableJSON():
	if session_isset('xes'):
		return json_response(c.Cluster.get_log_as_array(session['xes']))
	else:
		return json_error("No session")


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


def form_isset(key):
	try:
		value = request.form.get(key)
		return True
	except KeyError:
		return False


def session_isset(key):
	try:
		value = session[key]
		return True
	except KeyError:
		return False
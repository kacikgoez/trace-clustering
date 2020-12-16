import sys

sys.path.append("..")

import os
import time
import random

from flask import Flask, session, json, request, render_template, redirect
from pm4py.objects.log.importer.xes import importer as xes_importer

from trace_clustering.tclustering.cluster import Cluster
from trace_clustering.tclustering.measurements import Measurements
from trace_clustering.tclustering.logFunc import LogFunc

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "templates"))
app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), "uploads")
app.secret_key = 'Abraham Lincoln was the president of the United States'


@app.route('/')
def root():
    session.clear()
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_xes():
    if request.method == "POST":
        if 'file' not in request.files:
            return json_error("No file in request")
        file = request.files['file']
        if file.filename == '':
            return json_error("No selected file")
        if file and check_file_type(file.filename):
            filename = str(int(round(time.time() * 1000))) + ".xes"
            fpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(fpath)
            # algo, params, label, file_path
            # cluster= c.Cluster([0], ["Activity","Resource"], fpath)
            session["xes"] = fpath
            return redirect('select')


@app.route('/sample', methods=['GET', 'POST'])
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
            session["labels"] = json.loads(request.form.get("labels"))
            return redirect('result')
        return render_template('sample.html')
    return redirect("error")


@app.route('/select', methods=['GET', 'POST'])
def select():
    if not session_isset("xes"):
        return redirect("error")
    return render_template('select.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if (
            session_isset("selected")
            and session_isset("thresholds")
            and session_isset("labels")
            and session_isset("xes")
    ):
        c_obj = Cluster(get_path("spmf"), session["xes"], session["selected"], session["labels"], 0.8, ["CloFast", "SPAM", "SPAM"])
        cluster = c_obj.get_clustering(session["thresholds"])
        samples = (c_obj.get_sample_set()).get_sample_log()

        print("Result")
        measure = dict()
        measure["recall"] = Measurements.recall(samples, cluster)
        measure["precision"] = Measurements.precision(samples, cluster)
        measure["f1"] = Measurements.f1measure(samples, cluster)

        bundle = {"measures" : measure, "cluster" : LogFunc.get_log_as_array(cluster)}

        return json_response(bundle)
    return redirect("error")


@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('result.html')


@app.route('/error')
def error():
    return render_template("error.html")


@app.route('/table/json')
def table_json():
    if session_isset('xes'):
        log = LogFunc.get_log_as_array(xes_importer.apply(session['xes']))
        return json_response(log)
    else:
        return json_error("No session")


@app.route('/lib/bootstrap')
def provide_bootstrap():
    return app.response_class(response=render_template("js/bootstrap-4.5.2.min.js"), mimetype="text/javascript")

@app.route('/lib/jquery')
def provide_jquery():
    return app.response_class(response=render_template("js/jquery-3.5.1.min.js"), mimetype="text/javascript")


def run_server(p_debug=False):
    app.run(debug=p_debug, port=5001)


def json_error(msg):
    # Returns error message to user in JSON format
    return json_response({"status": "error", "message": msg})


def json_response(rsp):
    # Changes response type from HTML to JSON
    return app.response_class(response=json.dumps(rsp), mimetype="application/json")


def check_file_type(filename):
    # Checks file type, XES is currently the only one that's allowed
    return filename.lower().endswith('.xes')


def form_isset(key):
    try:
        # value = request.form.get(key)
        return True
    except KeyError:
        return False


def session_isset(key):
    try:
        if session[key] is None:
            return False
        return True
    except KeyError:
        return False

def get_path(to):
    to = to.lower()
    if to == "upload":
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), "uploads")
    elif to == "spmf":
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), "uploads", "processed")
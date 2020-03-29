from flask import Blueprint, request, Response
import uuid
import os
#from werkzeug import secure_filename
# For console debugging
import sys
import time
import random

# Custom modules
from AXIOME3_app.datahandle import luigi_prep_helper
from AXIOME3_app.datahandle import config_generator

# Celery task
from AXIOME3_app.tasks.pipeline import import_data_task

# Custom Exceptions
from AXIOME3_app.exceptions.exception import CustomError


blueprint = Blueprint("datahandle", __name__, url_prefix="/datahandle")

@blueprint.route("/", methods=['POST'])
def generate_files():
	form_type = request.form['formType']

	# Use UUID4 for unique identifier
	_id = str(uuid.uuid4())

	try:
		if(form_type == "InputUpload"):
			manifest_file = request.files["manifest"]
			input_format = request.form["Input Format"]
			sample_type = request.form["Sample Type"]
			# Do preliminary checks on manifest file
			manifest_path = luigi_prep_helper.input_upload_pre_check(
				_id=_id,
				uploaded_manifest=manifest_file,
				input_format=input_format
			)
			# Prepare necessary files for input upload
			log_config_path = luigi_prep_helper.pipeline_setup(_id)
			luigi_prep_helper.luigi_config_generator(
				_id=_id,
				log_config_path=log_config_path,
				manifest_path=manifest_path,
				sample_type=sample_type,
				input_format=input_format
			)
			# Run the pipeline
			import_data_task.apply_async(args=[_id])

	except CustomError as err:
		return err.response

	return Response("ok", status=200, mimetype='text/html')

@blueprint.route("/stream/")
def stream():
	def eventstream():
		while True:
			time.sleep(5);
			n = random.random()
			data = "data: This number, {}, is from the server!\n\n".format(str(n))
			yield data

	res = Response(eventstream(), mimetype="text/event-stream")
	# As of March 2020, there seems to be a bug with SSE in React
	# Need to set Cache-Control: no-transform if using proxy url
	# full URL would still work without this header.
	res.headers['Cache-Control'] = 'no-transform'
	
	return res
	#return "stream!"
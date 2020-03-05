from flask import Blueprint, request, jsonify, Response
import uuid
import json
import os
#from werkzeug import secure_filename
# For console debugging
import sys
import time

# Custom modules
from AXIOME3_app.datahandle import luigi_prep_helper
from AXIOME3_app.datahandle import config_generator

# Celery task
from AXIOME3_app.tasks.pipeline import dummy_task, move_log_task

# Messages
from AXIOME3_app.messages.message import (
	INTERNAL_SERVER_ERROR_MESSAGE
)

blueprint = Blueprint("datahandle", __name__, url_prefix="/datahandle")

def responseIfError(func, **kwargs):
	"""
	Executes a custom function, and returns an appropriate response
	if there is an error.

	Input:
		func: A function that returns status code and result.
		kwargs: keyword arguments to be passed to a custom function.
	"""
	code, result = func(**kwargs)
	if(code != 200):
		return Response(INTERNAL_SERVER_ERROR_MESSAGE, status=500, mimetype='text/html')

	return result

@blueprint.route("/", methods=['POST'])
def generate_files():
	form_type = request.form['formType']

	# Use UUID4 for unique identifier
	_id = str(uuid.uuid4())

	# Make sub output dir in /output
	responseIfError(luigi_prep_helper.make_output_dir, _id=_id)

	# Make sub output dir in /output
	responseIfError(luigi_prep_helper.make_log_dir, _id=_id)

	# Create luigi logging config file
	log_config_path = responseIfError(config_generator.make_log_config, _id=_id)

	# TODO
	# Store received files?
	# Make config file for luigi
	if(form_type == "InputUpload"):
		code, manifest_path = luigi_prep_helper.save_upload(_id, request.files["manifest"])
		code, new_manifest_path = luigi_prep_helper.reformat_manifest(_id, manifest_path)
		code, config_path = config_generator.make_luigi_config(_id, log_config_path, manifest=new_manifest_path)

	dummy_task.apply_async()

	return Response("ok", status=200, mimetype='text/html')
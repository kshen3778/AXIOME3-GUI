from AXIOME3_app.extensions import celery
import subprocess

from flask_socketio import SocketIO

from AXIOME3_app.tasks.utils import (
	log_status,
	emit_message,
	run_command,
	cleanup_error_message
)

@celery.task(name="pipeline.run.analysis")
def analysis_task(_id, URL, task_progress_file):
	local_socketio = SocketIO(message_queue=URL)
	channel = 'test'
	namespace = '/AXIOME3'
	room = _id

	isTaskDone = taxonomic_classification(
		socketio=local_socketio,
		channel=channel,
		namespace=namespace,
		task_progress_file=task_progress_file,
		room=room
	)

	if(isTaskDone == False):
		return

	isTaskDone = generate_asv_table(
		socketio=local_socketio,
		channel=channel,
		namespace=namespace,
		task_progress_file=task_progress_file,
		room=room
	)

	if(isTaskDone == False):
		return

	isTaskDone = pcoa_plots(
		socketio=local_socketio,
		channel=channel,
		namespace=namespace,
		task_progress_file=task_progress_file,
		room=room
	)

	if(isTaskDone == False):
		return

	message = "Done!"
	emit_message(
		socketio=local_socketio,
		channel=channel,
		message=message,
		namespace=namespace,
		room=room
	)
	log_status(task_progress_file, message)

def taxonomic_classification(socketio, room, channel, namespace, task_progress_file):
	message = 'Performing Taxonomic Classification...'
	emit_message(
		socketio=socketio,
		channel=channel,
		message=message,
		namespace=namespace,
		room=room
	)
	log_status(task_progress_file, message)

	cmd = ["python", "/pipeline/AXIOME3/pipeline.py", "Export_Taxa_Collapse", "--local-scheduler"]
	stdout, stderr = run_command(cmd)

	decoded_stdout = stdout.decode('utf-8')

	if("ERROR" in decoded_stdout):
		# pipeline adds <--> to the error message as to extract the meaningful part 
		if("<-->" in decoded_stdout):
			message = decoded_stdout.split("<-->")[1]
		else:
			message = decoded_stdout
		message_cleanup = 'ERROR:\n' + cleanup_error_message(message)
		emit_message(
			socketio=socketio,
			channel=channel,
			message=message_cleanup,
			namespace=namespace,
			room=room
		)
		log_status(task_progress_file, message_cleanup)

		return False

	return True

def generate_asv_table(socketio, room, channel, namespace, task_progress_file):
	message = 'Generating ASV Table...'
	emit_message(
		socketio=socketio,
		channel=channel,
		message=message,
		namespace=namespace,
		room=room
	)
	log_status(task_progress_file, message)

	cmd = ["python", "/pipeline/AXIOME3/pipeline.py", "Generate_Combined_Feature_Table", "--local-scheduler"]
	stdout, stderr = run_command(cmd)
	
	decoded_stdout = stdout.decode('utf-8')
	
	if("ERROR" in decoded_stdout):
		# pipeline adds <--> to the error message as to extract the meaningful part 
		if("<-->" in decoded_stdout):
			message = decoded_stdout.split("<-->")[1]
		else:
			message = decoded_stdout
		message_cleanup = 'ERROR:\n' + cleanup_error_message(message)
		emit_message(
			socketio=socketio,
			channel=channel,
			message=message_cleanup,
			namespace=namespace,
			room=room
		)
		log_status(task_progress_file, message_cleanup)

		return False

	return True

def pcoa_plots(socketio, room, channel, namespace, task_progress_file):
	message = 'Analyzing samples...'
	emit_message(
		socketio=socketio,
		channel=channel,
		message=message,
		namespace=namespace,
		room=room 
	)
	log_status(task_progress_file, message)

	cmd = ["python", "/pipeline/AXIOME3/pipeline.py", "PCoA_Plots", "--local-scheduler"]
	stdout, stderr = run_command(cmd)

	decoded_stdout = stdout.decode('utf-8')
	
	if("ERROR" in decoded_stdout):
		# pipeline adds <--> to the error message as to extract the meaningful part 
		if("<-->" in decoded_stdout):
			message = decoded_stdout.split("<-->")[1]
		else:
			message = decoded_stdout
		message_cleanup = 'ERROR:\n' + cleanup_error_message(message)
		emit_message(
			socketio=socketio,
			channel=channel,
			message=message_cleanup,
			namespace=namespace,
			room=room
		)
		log_status(task_progress_file, message_cleanup)

		return False

	cmd = ["python", "/pipeline/AXIOME3/pipeline.py", "PCoA_Plots_jpeg", "--local-scheduler"]
	stdout, stderr = run_command(cmd)
	
	decoded_stdout = stdout.decode('utf-8')
	
	if("ERROR" in decoded_stdout):
		# pipeline adds <--> to the error message as to extract the meaningful part 
		if("<-->" in decoded_stdout):
			message = decoded_stdout.split("<-->")[1]
		else:
			message = decoded_stdout
		message_cleanup = 'ERROR:\n' + cleanup_error_message(message)
		emit_message(
			socketio=socketio,
			channel=channel,
			message=message_cleanup,
			namespace=namespace,
			room=room
		)
		log_status(task_progress_file, message_cleanup)

		return False

	return True
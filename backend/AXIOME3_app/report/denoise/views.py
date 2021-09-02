from flask import Blueprint, request, send_file
import os

from AXIOME3_app.utils import get_denoise_dir

blueprint = Blueprint("denoise", __name__, url_prefix="/denoise")

@blueprint.route("/feature_table", methods=['POST'])
def denoise_feature_table():
	uid = request.form["uid"]
	DENOISE_DIR = get_denoise_dir(uid)

	if(uid == ''):
		# return sample output if uid not specified
		feature_table = os.path.join('/data/output/dada2/merged', 'merged_table.qza')
	else:
		feature_table = os.path.join(DENOISE_DIR, 'merged_table.qza')

	return send_file(feature_table, mimetype='application/octet-stream', as_attachment=True)

@blueprint.route("/representative_sequences", methods=['POST'])
def denoise_rep_seqs():
	uid = request.form["uid"]
	DENOISE_DIR = get_denoise_dir(uid)

	if(uid == ''):
		# return sample output if uid not specified
		rep_seqs = os.path.join('/data/output/dada2/merged', 'merged_rep_seqs.qza')
	else:
		rep_seqs = os.path.join(DENOISE_DIR, 'merged_rep_seqs.qza')

	return send_file(rep_seqs, mimetype='application/octet-stream', as_attachment=True)

@blueprint.route("/sample_summary/json", methods=['POST'])
def denoise_sample_summary():
	uid = request.form["uid"]
	DENOISE_DIR = get_denoise_dir(uid)

	if(uid == ''):
		# return sample output if uid not specified
		sample_summary = os.path.join('/data/output/dada2/', 'sample_counts.json')
	else:
		sample_summary = os.path.join(DENOISE_DIR, 'sample_counts.json')

	return send_file(sample_summary, mimetype='application/json', as_attachment=True)

@blueprint.route("/dada2/summary/json", methods=['POST'])
def dada2_summary():
	uid = request.form["uid"]
	DENOISE_DIR = get_denoise_dir(uid)

	if(uid == ''):
		# return sample output if uid not specified
		dada2_summary = os.path.join('/data/output/dada2/merged', 'merged_stats_dada2.json')
	else:
		dada2_summary = os.path.join(DENOISE_DIR, 'merged_stats_dada2.json')

	return send_file(dada2_summary, mimetype='application/json', as_attachment=True)

@blueprint.route("/summary_qzv", methods=['POST'])
def denoise_summary_qzv():
	uid = request.form["uid"]
	DENOISE_DIR = get_denoise_dir(uid)

	if(uid == ''):
		# return sample output if uid not specified
		stats_qzv = os.path.join('/data/output/dada2/merged', 'merged_stats_dada2.qzv')
	else:
		stats_qzv = os.path.join(DENOISE_DIR, 'merged_stats_dada2.qzv')

	return send_file(stats_qzv, mimetype='application/octet-stream', as_attachment=True)
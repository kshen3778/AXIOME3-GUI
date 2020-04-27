from flask import Blueprint, request, send_file
import sys
import os

blueprint = Blueprint("taxonomy", __name__, url_prefix="/taxonomy")

@blueprint.route("/collapse/tsv", methods=['GET', 'POST'])
def taxa_collapse_tsv():
	uid = request.form["uid"]
	taxa = request.form["taxa"]

	extension = ".tsv"
	# Absolute path to the metadata column json file
	collapsed_taxa = os.path.join('/data/output/taxa_collapse/', taxa + '_collapsed_table' + extension) # TEMP
	#collapsed_taxa = os.path.join('/output', uid, 'taxa_collapse', taxa + '_collapsed_table' + extension)	

	return send_file(collapsed_taxa, mimetype='text/tab-separated-values', as_attachment=True)

@blueprint.route("/collapse/qza", methods=['GET', 'POST'])
def taxa_collapse_qza():
	uid = request.form["uid"]
	taxa = request.form["taxa"]

	extension = ".qza"
	# Absolute path to the metadata column json file
	collapsed_taxa = os.path.join('/data/output/taxa_collapse/', taxa + '_collapsed_table' + extension) # TEMP
	#collapsed_taxa = os.path.join('/output', uid, 'taxa_collapse', taxa + '_collapsed_table' + extension)	

	return send_file(collapsed_taxa, mimetype='application/octet-stream', as_attachment=True)

@blueprint.route("/asv/tsv", methods=['GET', 'POST'])
def taxa_asv_tsv():
	uid = request.form["uid"]

	extension = ".tsv"
	# Absolute path to the metadata column json file
	asv_taxa = os.path.join('/data/output/exported/', "taxonomy" + extension) # TEMP
	#asv_taxa = os.path.join('/output', uid, 'exported', "taxonomy" + extension)	

	return send_file(asv_taxa, mimetype='text/tab-separated-values', as_attachment=True)

@blueprint.route("/asv/qza", methods=['GET', 'POST'])
def taxa_asv_qza():
	uid = request.form["uid"]

	extension = ".qza"
	# Absolute path to the metadata column json file
	asv_taxa = os.path.join('/data/output/taxonomy/', "taxonomy" + extension) # TEMP
	#asv_taxa = os.path.join('/output', uid, 'taxonomy', "taxonomy" + extension)	

	return send_file(asv_taxa, mimetype='application/octet-stream', as_attachment=True)
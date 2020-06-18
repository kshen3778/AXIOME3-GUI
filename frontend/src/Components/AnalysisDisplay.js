import React, { useEffect } from 'react';
import { connect } from 'react-redux';

import { getUploadField } from '../redux/actions/uploadAction'
// Option redux
import { updateOptionList } from '../redux/actions/optionAction'
// Submit redux
import { updateFormType } from '../redux/actions/submitAction'

import AXIOME3Template from './AXIOME3Template'
// Analysis description
import AnalysisDescription from './Description/AnalysisDescription';
// Analysis options
import AnalysisOption from './data/AnalysisOption'
// Form type
import { ANALYSIS_FORMTYPE } from '../misc/FormTypeConfig';

function AnalysisDisplay(props) {
	// Redux actions
	const { getUploadField, updateOptionList, updateFormType } = props

	useEffect(() => {
		console.log(props.uid)
		const uploadField = [
			{id: 0, name: "feature-table", file: "", label: "Feature Table (.qza)"},
			{id: 1, name: "rep-seqs", file: "", label: "Representative sequences (.qza)"},
			{id: 2, name: "metadata", file: "", label: "Metadata (.tsv)"}
		]

		// Get upload elements
		getUploadField(uploadField)

		// Get option list
		updateOptionList(AnalysisOption)

		// Update form type
		updateFormType(ANALYSIS_FORMTYPE)
	}, [])
	
	const description = <AnalysisDescription/>

	return (
		<React.Fragment>
			<AXIOME3Template
				description={description}
				isExtension={false}
			/>
		</React.Fragment>
	)
}

const mapStateToProps = state => ({
	options: state.option.options,
	uid: state.submit.uid
})

const mapDispatchToProps = {
	getUploadField,
	updateOptionList,
	updateFormType,
}

export default connect(mapStateToProps, mapDispatchToProps)(AnalysisDisplay)
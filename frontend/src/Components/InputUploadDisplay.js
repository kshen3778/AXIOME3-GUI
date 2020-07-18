import React, { useEffect } from 'react';
import { connect } from 'react-redux';

import AXIOME3Template from './AXIOME3Template'

// Import option interface data
import InputUploadOption from './data/InputUploadOption';

// Module description
import InputUploadDescription from './Description/InputUploadDescription'

// Upload redux
import { getUploadField } from '../redux/actions/uploadAction'
// Option redux
import { updateOptionList } from '../redux/actions/optionAction'
// Submit redux
import { updateFormType } from '../redux/actions/submitAction'
// Form type
import { INPUT_UPLOAD_FORMTYPE } from '../misc/FormTypeConfig';
// Upload field names
import { MANIFEST_FILE } from '../misc/InputUploadNameConfig';

/**
 * Main componenet that concerns with Input Upload module.
 */
function InputUploadDisplay(props) {
	// Redux actions
	const { getUploadField, updateOptionList, updateFormType } = props

	useEffect(() => {
		const uploadField = [
			{id: 0, name: MANIFEST_FILE, label: "Manifest File (.txt, .tsv, .csv)", acceptedExtensions: ".txt,.tsv,.csv"}
		]
		// Get upload elements
		getUploadField(uploadField)

		// Get option list
		updateOptionList(InputUploadOption)

		// Update form type
		updateFormType(INPUT_UPLOAD_FORMTYPE)
	}, [])

	// Type of the form;
	// For server side processing
	const description = <InputUploadDescription />

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
	options: state.option.options
})

const mapDispatchToProps = { 
	getUploadField,
	updateOptionList,
	updateFormType,
}

export default connect(mapStateToProps, mapDispatchToProps)(InputUploadDisplay)

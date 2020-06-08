import React, { useEffect } from 'react'
import { connect } from 'react-redux';
import { Link, withRouter } from 'react-router-dom';

import UploadElementsMain from './Upload-Elements/UploadElementsMain'
import DescriptionMain from './Description/DescriptionMain'
import OptionsMain from './Options/OptionsMain'
import TabBarMain from './TabBar/TabBarMain'
import StatusMain from './Status/StatusMain'
import SubmitButton from './SubmitButton/SubmitButton'
// Custom helper functions
import { handleSubmit } from './SubmitButton/SubmitHelper'

import { getUid } from '../redux/actions/downloadAction'
// Submit redux
import { submitData, resetFileUploadProgress, resetAnalysis, resetRetrieve, resetFormType, resetUid } from '../redux/actions/submitAction'
// Upload redux
import { emptySelectedFiles, emptyFiles } from '../redux/actions/uploadAction'
// Option redux
import { resetOptions, resetSelectedOptions } from '../redux/actions/optionAction'
// RemoteWorker redux
import { resetSessionId, resetRemoteWorker } from '../redux/actions/remoteWorkerAction'

import {
	REPORT_BASE_ROUTE,
} from '../RouteConfig';

function MainDisplayTemplate(props) {
	const subDisplayStyles = {
		background: "#DCDCDC",
		margin: "auto",
		padding: "5%"
	}
	// Redux state
	const { formType, selectedFiles, selectedOptions } = props;

	// props from parent component
	const { description } = props;

	// Submit redux actions
	const { submitData, resetFileUploadProgress, resetAnalysis, resetRetrieve, resetFormType, resetUid } = props;

	// Upload redux actions
	const { emptySelectedFiles, emptyFiles } = props;

	// Option redux action
	const { resetSelectedOptions, resetOptions } = props;

	// RemoteWorker redux action
	const { resetSessionId, resetRemoteWorker } = props;

	// Session ID
	const { uid } = props;

	useEffect(() => {
		// Reset selected files
		emptySelectedFiles()

		// Reset server-browsed files
		emptyFiles()

		// Reset options
		resetOptions()

		// Reset selected options
		resetSelectedOptions()

		// Reset Analysis submit
		resetAnalysis()

		// Reset session retrieve submit
		resetRetrieve()

		// Reset input session id
		resetSessionId()

		// Reset form type
		resetFormType()

		// Clean up
		return () => {
			// Reset worker messages
			resetRemoteWorker()

			// Reset UID
			resetUid()
		}
	}, [])

	const formTypeRoute = 'formType=' + formType;
	const uidRoute = 'uid=' + uid;
	var reportRoute = REPORT_BASE_ROUTE + '?' + uidRoute + '&' + formTypeRoute
	// Append options to query string
	Object.keys(selectedOptions).forEach(k => {
		reportRoute = reportRoute + '&' + k + '=' + selectedOptions[k]
	});

	return (
		<div className="main-display">
			<TabBarMain/>
			<div className="sub-display" style={subDisplayStyles}>
				<form onSubmit={(e) => {handleSubmit(e, formType, selectedFiles, selectedOptions, submitData)}}>
					<DescriptionMain description={description}/>
					<UploadElementsMain />
					<OptionsMain />
					<SubmitButton />
				</form>
			</div>
			<StatusMain/>
			<Link to={reportRoute}>
				Hello
			</Link>
		</div>
	)
}

const mapStateToProps  = state => ({
	uid: state.submit.uid,
	selectedFiles: state.upload.selectedFiles,
	selectedOptions: state.option.selectedOptions,
	formType: state.submit.formType,
})

const mapDispatchToProps = {
	emptySelectedFiles,
	emptyFiles,
	resetSelectedOptions,
	resetOptions,
	submitData,
	resetFileUploadProgress,
	resetAnalysis,
	resetRetrieve,
	resetSessionId,
	resetFormType,
	resetRemoteWorker,
	resetUid,
}

export default connect(mapStateToProps, mapDispatchToProps)(MainDisplayTemplate)

//<a href='#' onClick={() => {props.history.push('/tmp')}}>Click to view report</a>
/*
<span
				className="clickable"
				onClick={() => {handleClick(formType, REPORT_ROUTE)}}
			>
				Click to view report
			</span>
			*/
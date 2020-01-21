import React from 'react'
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import OptionDetailsItem from './OptionDetailsItem'

/**
 * Container for detail view for each type of option: basic and advanced.
 */
function OptionDetails(props) {
	// String specifying which type of option it is (e.g. basicOptions or advancedOptions)
	// These can be used to access respective items in the redux state
	const { optionType } = props

	// Redux state storing list of options
	const { options } = props

	let optionDetails
	if(options[optionType]) {
		optionDetails = options[optionType].keys.map(k => {
			const id = optionType + "_" + k
			return(
				<OptionDetailsItem
					label={options[optionType].entities[k].label}
					key={id}
				/>
			)
		})
	} else {
		optionDetails = []
	}

	return(
		<div className="option-detail-container">
			{optionDetails}
		</div>
	)
}

OptionDetails.propTypes = {
  options: PropTypes.object.isRequired,
}

const mapStateToProps = state => ({
	options: state.option.options
})

export default connect(mapStateToProps)(OptionDetails)
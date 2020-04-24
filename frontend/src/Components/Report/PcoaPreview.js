import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { connect } from 'react-redux';

function PcoaPreview(props) {
	const [ source, setSource ] = useState('')

	// States from parent component
	const { columns, distanceTypes, columnOptionValue, distanceOptionValue } = props;

	// Event handler from parent component
	const { handleChange } = props;

	// UUID
	const { uid } = props;

	// Whenever dropdown value changes, make API request
	useEffect(() => {
		const pcoaImageEndpoint = '/report/pcoa'
		const getPcoaImage = async () => {
			const formData = new FormData();

			formData.append('uid', uid);
			formData.append('distance', distanceTypes[distanceOptionValue]);
			formData.append('column', columns[columnOptionValue]);

			const configOptions = {
				url: pcoaImageEndpoint,
				method: 'post',
				data: formData,
				responseType: 'arraybuffer'
			}
			const res = await axios(configOptions);

			const base64 = btoa(
				new Uint8Array(res.data).reduce( 
					(data, byte) => data + String.fromCharCode(byte), '' 
					)
				)

			setSource(base64)
		};

		if (Object.keys(columns).length !== 0 && Object.keys(distanceTypes).length !== 0) {
			getPcoaImage();
		}
	}, [distanceOptionValue, columnOptionValue])

	const columnOptions = Object.keys(columns).map(column => {
		return(
			<option value={column} key={column}>{column}</option>
		)
	})
	const distanceOptions = Object.keys(distanceTypes).map(distanceType => {
		return(
			<option value={distanceType} key={distanceType}>{distanceType}</option>
		)
	})

	return(
		<div>
			<select
				name='distanceType'
				onChange={handleChange}
				value={distanceOptionValue}
			>
				{distanceOptions}
			</select>
			<select
				name='columnType'
				onChange={handleChange}
				value={columnOptionValue}
			>
				{columnOptions}
			</select>
			<img src={`data:image/jpeg;base64,${source}`} />
		</div>
	)
}

const mapStateToProps  = state => ({
	uid: state.download.uid
})

const mapDispatchToProps = {
	
}

export default connect(mapStateToProps, mapDispatchToProps)(PcoaPreview)
from AXIOME3_app.app import create_app, socketio

app = create_app(debug=True, development=True)

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=5000)
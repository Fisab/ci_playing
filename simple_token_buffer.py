from flask import Flask, request, jsonify
import logging

app = Flask(__name__)


GITHUB_TOKEN = 'helloworld'


@app.route('/', methods=['GET'])
def index():
	return 'OK', 200


@app.route('/retrieve_token', methods=['GET'])
def retrieve_token():
	return GITHUB_TOKEN


@app.errorhandler(500)
def server_error(e):
	logging.exception('An error occurred during a request.')
	return """
	An internal error occurred: <pre>{}</pre>
	See logs for full stacktrace.
	""".format(e), 500


if __name__ == '__main__':
	app.run(debug=True, port=887, host='0.0.0.0')


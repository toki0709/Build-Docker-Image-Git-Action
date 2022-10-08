import json
import logging
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    """
    Simple API response
    """
    logging.info("Main request successful")
    return "Hello World!"


@app.route("/status")
def status():
    """
    return app status.
    """
    logging.info("Health status is OK")
    return app.response_class(response=json.dumps({"result": "OK - healthy"}), status=200, mimetype='application/json')


@app.route('/metrics')
def metrics():
    """
    returns app metrics
    """
    logging.info("Metrics Status is successful")
    return app.response_class(response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}), status=200, mimetype='application/json')


if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')

import os
import json

from flask import Flask, render_template, jsonify
from prometheus_flask_exporter import PrometheusMetrics

from logger import init_logger

VISITS_FILE = 'db/visits.json'

app = Flask(__name__)
metrics = PrometheusMetrics(app)
logger = init_logger()


@app.route("/")
def home():
    logger.info('GET /')
    if not os.path.exists(VISITS_FILE):
        json.dump({"visits": "1"}, open(VISITS_FILE, 'w'))
    else:
        visits = int(json.load(open(VISITS_FILE))["visits"])
        json.dump({"visits": str(visits + 1)}, open(VISITS_FILE, 'w'))
    return render_template('index.html')


@app.route("/visits")
def visitor_count():
    if not os.path.exists(VISITS_FILE):
        return jsonify({"visits": "0"})
    return jsonify(json.load(open(VISITS_FILE)))


# When executing `python app.py` instead of `flask run`
if __name__ == "__main__":
    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True, host='127.0.0.1', port=5000)

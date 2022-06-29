from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return render_template('index.html')


# Debug mode
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)

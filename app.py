import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    pod_name = os.environ.get("HOSTNAME", "Unknown Pod")
    return f"<h1>Hello from Kubernetes!</h1><p>Served by Pod: <b>{pod_name}</b></p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
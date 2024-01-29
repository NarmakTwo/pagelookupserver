from flask import Flask, redirect
import json

app = Flask(__name__)

@app.route('/<path:subpath>')
def catch_all(subpath):
    with open("pagelookup.json") as f:
        data = json.load(f)
    if subpath in data:
        return redirect(f"http://{data[subpath]}")
    else:
        return "Page not found", 404

app.run(host='0.0.0.0', port=10000)

from pathlib import Path
from flask import Flask, request

app = Flask(__name__)

OUTPUT = Path("received")
OUTPUT.mkdir(exist_ok=True)


@app.post("/collect")
def collect():
    uploaded = request.files["file"]
    uploaded.save(OUTPUT / uploaded.filename)
    return {"status": "ok"}

app.run(host="127.0.0.1", port=8080)
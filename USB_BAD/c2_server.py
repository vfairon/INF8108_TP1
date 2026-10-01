from pathlib import Path
from flask import Flask, request

app = Flask(__name__)

OUTPUT = Path("received")
OUTPUT.mkdir(exist_ok=True)


@app.post("/collect")
def collect():
    data = request.get_json()

    with open(OUTPUT / "data.txt", "a") as f:
        f.write(f"{data}\n")

    return {"status": "ok"}


app.run(host="0.0.0.0", port=8080)
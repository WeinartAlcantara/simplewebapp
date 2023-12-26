from flask import Flask
import os

app = Flask(__name__)

color = os.getenv("COLOR", "#FFFFFF")

@app.route("/")
def hello():
    return jsonify({"message": "Hello from Flask!", "color": color})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

from flask import Flask, render_template, jsonify
import os

app = Flask(__name__, template_folder="templates")

color = os.getenv("COLOR", "#FFFFFF")

@app.route("/")
def hello():
    return render_template("index.html", message="Hello from Flask!", "color":color)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

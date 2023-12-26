from flask import Flask, render_template
import os
import random

app = Flask(__name__, template_folder="templates")

# Generate a random color
random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

color = os.getenv("COLOR", random_color)

@app.route("/")
def index():
    return render_template("index.html", message="Hello from Flask!", color=color)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

from flask import Flask, render_template
import random


app = Flask(__name__, template_folder="templates")

random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

color = random_color

messages = [
    "Canary1",
    "Canary1",
    "Canary1",
    "Canary1",
    "Canary1"
]


@app.route("/")
def index():
    random_message = random.choice(messages)
    return render_template("index.html", message=random_message, color=color)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

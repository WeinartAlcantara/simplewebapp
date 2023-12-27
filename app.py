from flask import Flask, render_template
import os
import random

app = Flask(__name__, template_folder="templates")

# Generate a random color
color = os.getenv("COLOR", random_color)

# List of possible messages
messages = [
    "Hello from Weinartzz!",
    "Welcome to our simple web App for the CI/CDz!",
    "Greetings, from Shienz!",
    "Lloyd says hiz!",
    "Happy new yearz!"
]

@app.route("/")
def index():
    random_message = random.choice(messages)
    return render_template("index.html", message=random_message, color=color)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

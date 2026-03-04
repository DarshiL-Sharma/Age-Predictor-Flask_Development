import random
import requests
from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.datetime.now().year
    random_number = random.randint(0, 9)
    return render_template("home.html",
                           num=random_number,
                           date=current_time)

@app.route('/name/<name>')
def finding_name(name):
    response = requests.get("https://api.agify.io", params={"name": name})
    data = response.json()

    return render_template(
        "index.html",
        name=data["name"],
        age=data["age"]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

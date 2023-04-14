from flask import Flask, render_template

app = Flask("Weather")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/services/")
def services():
    return render_template("services.html")


app.run(debug=True)

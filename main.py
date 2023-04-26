from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/services/")
def services():
    return render_template("services.html")


@app.route("/blogs/")
def blogs():
    return render_template("blogs.html")


@app.route("/api/v1/<station>/<date>")
def data(station, date):
    filename = f"data-small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station, "date": date, "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True, port=5000)

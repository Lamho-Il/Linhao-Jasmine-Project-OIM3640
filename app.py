from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return "<h1>Contact Page</h1><p>This page is under construction.</p>"


@app.route("/submit", methods=["GET", "POST"])
def submit():
    return "<h1>Submit Page</h1><p>This page is under construction.</p>"


if __name__ == "__main__":
    app.run(debug=True)

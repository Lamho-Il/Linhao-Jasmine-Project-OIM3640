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


def get_compatibility_score(user_data, groupmate_data):
    pass
    # Openai API


@app.route("/submit", methods=["GET", "POST"])
def submit():
    user_mbti = request.form["mbti"]
    user_astro = request.form["astro"]
    results = []

    # 4 groupmates/ groupsize: 5 in max
    print(f"User MBTI: {user_mbti}, User Astro: {user_astro}")

    for i in range(1, 5):  # 4 groupmates
        groupmate_mbti = request.form.get(f"groupmate{i}_mbti")
        groupmate_astro = request.form.get(f"groupmate{i}_astro")
        if groupmate_mbti and groupmate_astro:
            compatibility = "placeholder"
            results.append(
                {
                    "mbti": groupmate_mbti,
                    "astro": groupmate_astro,
                    "compatibility": compatibility,
                }
            )
            print(
                f"Groupmate {i}: MBTI: {groupmate_mbti}, Astro: {groupmate_astro}, Compatibility: {compatibility}"
            )

    if not results:
        print("No groupmate data received.")

    return render_template("results.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)

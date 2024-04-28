from flask import Flask, render_template, request 
import os

import openai
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

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


def get_compatibility_score(user_mbti, user_astro, groupmate_mbti, groupmate_astro):
    prompt = f"Assess compatibility between a person with MBTI {user_mbti} and astrological sign {user_astro} and another person(s) with MBTI {groupmate_mbti} and astrological sign {groupmate_astro}."

    try:
        response = openai.Completion.create(
            model = "gpt-3.5-turbo-instruct",
            prompt = prompt,
            max_tokens = 150,
            temperature=0.7,
            api_key = OPENAI_API_KEY)
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "Error in generating compatibility result."


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        user_mbti = request.form["mbti"]
        user_astro = request.form["astro"]
        results = []

        print(f"User MBTI: {user_mbti}, User Astro: {user_astro}")

        for i in range(3):  # 3 groupmates
            groupmate_mbti = request.form.get(f"groupmate{i}_mbti")
            groupmate_astro = request.form.get(f"groupmate{i}_astro")
            if groupmate_mbti and groupmate_astro:
                compatibility = get_compatibility_score(user_mbti, user_astro, groupmate_mbti, groupmate_astro)
                results.append(
                    {
                        "mbti": groupmate_mbti,
                        "astro": groupmate_astro,
                        "compatibility": compatibility
                    }
                )
                # print(f"Groupmate {i}: MBTI: {groupmate_mbti}, Astro: {groupmate_astro}, Compatibility: {compatibility}")

        if not results:
            print("No groupmate data received.")

        return render_template("results.html", results=results)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

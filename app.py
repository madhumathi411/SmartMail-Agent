from flask import Flask, render_template, request, redirect, session

from agents.email_analyzer import analyze_email
from agents.priority_agent import assign_priority
from agents.context_agent import get_context
from agents.response_agent import generate_response

from database.database import create_tables, save_analysis


app = Flask(__name__)

app.secret_key = "smartmail-secret-key"


# Create database tables when the application starts
create_tables()


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        if email and password:

            session["user"] = email

            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template("dashboard.html")


@app.route("/inbox")
def inbox():

    if "user" not in session:
        return redirect("/")

    return render_template("inbox.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "user" not in session:
        return redirect("/")

    email_text = request.form.get("email_text", "")

    analysis = analyze_email(email_text)

    intent = analysis["intent"]

    priority = assign_priority(
        email_text,
        intent
    )

    context = get_context(intent)

    response = generate_response(
        intent,
        context,
        email_text
    )

    confidence = 0.90

    save_analysis(
        email_id=0,
        intent=intent,
        priority=priority,
        confidence=confidence,
        response=response
    )

    return render_template(
        "email.html",
        email_text=email_text,
        intent=intent,
        priority=priority,
        context=context,
        response=response,
        confidence=confidence
    )


@app.route("/review")
def review():

    if "user" not in session:
        return redirect("/")

    return render_template("review.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

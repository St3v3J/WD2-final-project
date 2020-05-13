from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/contract", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template("success.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


if __name__ == '__main__':
    app.run()
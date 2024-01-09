from flask import Flask, render_template, redirect, request, session

from controller import *
from flask_session import Session

app = Flask(__name__, template_folder="view", static_folder="view/static")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_PERMANENT"] = "filesystem"
Session(app)


@app.route("/")
def home():
    return render_template("signin.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        status, data = CustomerController.login(username, password)
        if status:
            session["username"] = username
            return render_template("signin.html", profile=data)
        else:
            message = data
    return render_template("index.html", message=message)

@app.route("/customer", methods=["POST", "GET", "DELETE"])
def customer():
    if not session.get("username"):
        return render_template("signin.html")

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_family = request.form.get("last_family")
        email = request.form.get("email")
        password = request.form.get("password")
        status, data = CustomerController.save(first_name,last_family,email, password)
    elif request.method == "DELETE":
        CustomerController.remove(request.args.get("id"))

    # return data, 204
    return render_template("customer.html", profile=CustomerController.find_by_email(session.get("email"))[1])


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # if request.form.get("password") == request.form.get("repeat_password"):

        status, data = CustomerController.save(
            request.form.get("name"),
            request.form.get("family"),
            request.form.get("email"),
            request.form.get("password"))


        return render_template("signup.html")




@app.route("/forget")
def forget():
    return render_template("forget-password.html")

if __name__ == "__main__":
    app.run(debug=True)



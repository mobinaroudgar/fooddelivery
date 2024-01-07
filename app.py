from flask import Flask, render_template, redirect, request, session
from flask_session import Session

from controller import *

app = Flask(__name__, template_folder="view", static_folder="view/static")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        status, data = CustomerController.login(email, password)
        if status:
            session["email"] = email
            return render_template("customer.html", profile=data)
        else:
            message = data
    return render_template("login.html", message=message)


@app.route("/customer", methods=["POST", "GET", "DELETE"])
def customer():
    if not session.get("email"):
        return render_template("login.html")

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_family = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        status, data = CustomerController.save(first_name, last_family, email, password)
    elif request.method == "DELETE":
        CustomerController.remove(request.args.get("id"))

    # return data, 204
    return render_template("customer.html", customer=CustomerController.find_by_email(session.get("email"))[1])


@app.route("/signup", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # if request.form.get("password") == request.form.get("repeat_password"):

        status, data = CustomerController.save(
            request.form.get("first_name"),
            request.form.get("last_name"),
            request.form.get("email"),
            request.form.get("password"))
        return render_template("login.html")


    return render_template("signup.html")

@app.route("/forgot")
def forget():
   # if request.method == "POST":
    #if request.form.get("password") == request.form.get("forget_password"):
         #status , data = CustomerController.save(
        # request.form.get("password")
 return render_template("forgot-password.html")


#@app.route("/logout")
#def logout():
   # session["username"] = None
    #return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, redirect, request, session

from controller import *
from flask_session import Session

app = Flask(__name__, template_folder="view", static_folder="view/static")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("signup.html")
@app.route("/index")
def back():
    return render_template("index.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/home",methods=["POST", "GET"])
def home():
    status, orders = FoodOrderController.find_by_customer_id(session.get("id"))
    return render_template("home.html", orders = orders)

@app.route("/order", methods=["POST", "GET"])
def order():
    if not session.get("orders"):
        return render_template("order.html")
    if request.method == "POST":
        pass
    return render_template("index.html", orders=CustomerController.find_by_customer_id(session.get("customer_id"))[1].orders)

@app.route("/manageproduct", methods=["POST", "GET"])
def manageproduct():
    if not session.get("username"):
        return render_template("manage-product.html")
    if request.method == "POST":
        pass
    return render_template("index.html", orders=CustomerController.find_by_customer_id(session.get("customer_id"))[1].orders)


@app.route("/login", methods=["POST", "GET"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        status, data = CustomerController.login(email, password)
        if status:
            session["email"] = email
            session["id"] = data.id
            return render_template("index.html", profile=data)
        else:
            message = data
    return render_template("login.html", message=message)

@app.route("/customer", methods=["POST", "GET", "DELETE"])
def customer():
    # if not session.get("email"):
    #     return render_template("login.html")

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_family = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        status, data = CustomerController.save(first_name,last_family,email, password)
        print(status,data)
    elif request.method == "DELETE":
        CustomerController.remove(request.args.get("id"))

    # return data, 204
    return render_template("signup.html", customer=CustomerController.find_all())
#@app.route("/food_order",methods=["POST","GET"])
#def food_order():
 #   if not session.get("customer"):
  #      return render_template("home")



#@app.route("/signup", methods=["POST", "GET"])
#def signup():
 #   if request.method == "POST":
        # if request.form.get("password") == request.form.get("repeat_password"):

  #      status, data = CustomerController.save(
   #         request.form.get("name"),
    #        request.form.get("family"),
     #       request.form.get("email"),
      #      request.form.get("password"))

       # return render_template("login.html")

    #return render_template("signup.html")

#@app.route("/search")
#def search():
    #query = request.args.get("query")
    #results = f"you searched for : {query}"
   # return results


#@app.route("/forget")
#def forget():
 #   return render_template("forget-password.html")

#@app.route("/logout")
#def logout():
 #   session["username"] = None
  #  return redirect("/")
   # return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)



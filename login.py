from flask import Flask,request,render_template,url_for,redirect
app= Flask(__name__) #app is instance of flask class
@app.route("/") #Decorator
# def hello_world():
#     return "<p>Hello World!</p>"
def new_function():
    return render_template("index.html")
@app.route("/login",methods=["POST","GET"]) #decorator
def login():
    if request.method=="POST":
        user=request.form("nm")
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")
@app.route("/<user>")
def user(usr):
    return "<h1>Welcome{user}</h1>"
if __name__ == "__main__":
    app.run(debug=True,port=8000)
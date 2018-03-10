#Remember


from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/loginpage") 
def loginpage():
    return render_template("loginpage.html")

@app.route('/afterlogin2')
def afterlogin2():
    return render_template("afterlogin2.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

if __name__ == '__main__':
   app.run(debug = True)

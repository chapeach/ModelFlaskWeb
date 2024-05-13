from flask import Flask,session, render_template, redirect
from datetime import timedelta

from app_login import *
from app_setting import *

app = Flask(__name__)
app.secret_key = "12345"
app.permanent_session_lifetime = timedelta(minutes=100)
app.register_blueprint(app_login)
app.register_blueprint(app_setting)

@app.route("/")
def Home():
    if "UserId" not in session:
        return redirect("/login")
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
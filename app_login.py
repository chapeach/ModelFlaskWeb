from flask import Blueprint, session, render_template, redirect, request
import sqlite3

app_login = Blueprint('app_login', __name__)

@app_login.route('/login')
def Login():
    if "UserId" not in session:
        return render_template("/login/login.html")
    else:
        return redirect("/")

@app_login.route('/fn_login', methods = ["POST"])
def Fn_login():
    if request.method == "POST":
        try:
            userId = request.form["userId"]
            password = request.form["password"]
            con = sqlite3.connect("db/db.db")
            cur = con.cursor()
            sql = 'SELECT * FROM userlogin WHERE userId = "{}" AND password = "{}"'.format(userId, password)
            data1 = cur.execute(sql)
            data1 = data1.fetchall()
            data1 = list(data1[0])

            if len(data1) == 5:
                if data1[4] == "1":
                    session['UserId'] = data1[1]
                    session['Password'] = data1[2]
                    session['Level'] = data1[3]
                    return redirect("/")

        except:
            pass
    return redirect("/")
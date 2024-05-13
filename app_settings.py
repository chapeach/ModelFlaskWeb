from flask import Blueprint, session, render_template, redirect, request
import sqlite3

app_settings = Blueprint('app_settings', __name__)

# page
@app_settings.route('/settings/userlogin')
def User_login():
    try:
        con = sqlite3.connect("db/db.db")
        cur = con.cursor()

        sql = 'SELECT userId, level, status FROM userlogin'
        data1 = cur.execute(sql)
        data1 = data1.fetchall()

        sql_list_level = 'SELECT level FROM list_level'
        data_list_level = cur.execute(sql_list_level)
        data_list_level = data_list_level.fetchall()

        con.close()
    except:
        pass
    return render_template("/settings/userlogin.html", data1=data1, data_list_level=data_list_level)

# fn
@app_settings.route('/settings/userlogin/addUser', methods = ["POST"])
def User_login_adduser():
    try:
        userId = request.form["userId"]
        password = request.form["password"]
        level = request.form["level"]

        con = sqlite3.connect("db/db.db")
        cur = con.cursor()

        sql_userlogin_adduser = 'INSERT INTO userlogin (userId, password, level, status) VALUES ("{}","{}","{}","{}")'.format(userId, password, level, "disable")
        print(sql_userlogin_adduser)
        data1 = cur.execute(sql_userlogin_adduser)

        con.commit()
        con.close()
    except:
        pass
    return redirect('/settings/userlogin')
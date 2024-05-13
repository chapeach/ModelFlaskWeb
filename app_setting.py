from flask import Blueprint, session, render_template, redirect, request
import sqlite3

app_setting = Blueprint('app_setting', __name__)

@app_setting.route('/userlogin')
def User_login():
    return render_template("/setting/userlogin.html")
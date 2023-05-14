from flask import render_template, url_for, flash, redirect, request,abort
from carparking import app
from flask_login import login_user, current_user, logout_user, login_required


from carparking import app
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/navbar")
def navbar():
    return render_template('navbar.html')



@app.route("/register", methods=['GET', 'POST'])
def register():
   
    return render_template('register.html', title='Register')


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Login')

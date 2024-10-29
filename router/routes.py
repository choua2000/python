from flask import Flask, render_template, request, redirect, url_for, session, flash,send_from_directory
from app import app
from database import *
from router.userRoute import *
from router.dashboradRoute import *
from router.productRoute import *


@app.route('/')
@app.route('/home')
def home():
    pass
    return render_template('home.html')
@app.route('/about')
def about():
    pass
    return render_template('about.html')

@app.route('/service')
def service():
    pass
    return render_template('service.html')

@app.route('/contact')
def contact():
    pass
    return render_template('contact.html')

@app.route('/index')
def index():
    pass
    return render_template('index.html')
@app.route('/register')
def register():
    pass
    return render_template('register.html')
@app.route('/add_user_1', methods=['POST'])
def add_user_1():
    with getcursorTO() as cur:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        tel = request.form['tel']
        email = request.form['email']
        password = request.form['password']
        sql = """INSERT INTO user_1(firstname,lastname,tel,email,password)
                VALUES (%s,%s,%s,%s,%s);"""
        cur.execute(sql, (firstname,lastname,tel,email,password))
        flash('success')
    return render_template('index.html')
    
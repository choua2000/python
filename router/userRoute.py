from flask import Flask, render_template, request, redirect, url_for, session, flash,send_from_directory
from app import app
from database import *

@app.route('/Signup')
def Signup():
    pass
    return render_template('Signup.html')

@app.route('/add_signup_user', methods=['POST'])
def add_signup_user():
    with getcursorTO() as cur:
        if request.method == 'POST':
            # id = request.form['id']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            password = request.form['password']
            tel = request.form['tel']
            sql = """INSERT INTO users(firstname,lastname,email,password,tel)
                    VALUES (%s,%s,%s,%s,%s);"""
            cur.execute(sql, (firstname, lastname, email, password, tel))
            flash('success')
        return render_template('home.html')

@app.route('/login_user')
def login_user():
    pass
    return render_template('Login.html')
@app.route('/login', methods=['POST'])
def login():
    with getcursorTO() as cur:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            sql = """SELECT * FROM users WHERE email = %s AND password = %s;"""
            cur.execute(sql, (email, password))
            result = cur.fetchall()
            if result:
                flash('success')
                return render_template('home.html')
            else:
                flash('fail')
                return render_template('Login.html')

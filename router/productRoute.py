from flask import Flask, render_template, request, redirect, url_for, session, flash,send_from_directory
from database import *
from uuid import *
from app import app

@app.route('/product')
def product():
    with getcursorTO() as cur:
     sql = """SELECT id,name,description,price,stock_quantity FROM products;"""
    cur.execute(sql)
    result = cur.fetchall()
    return render_template('backend/product.html',result=result)
@app.route('/searchs', methods=['GET'])
def searchS():
    if request.method == 'POST':
        id=request.form.get('hear')
    elif request.method == 'GET':
        id=request.form.get('hear')
    with getcursorTO() as cur:
     sql = """SELECT id,name,description,price,stock_quantity FROM products where name like %s;"""
    cur.execute(sql,(id,))
    result = cur.fetchall()
    return render_template('backend/where.html',result=result)
@app.route('/add_product',methods=['POST','GET'])
def add_product():
    pass
    return render_template('backend/add_product.html')
@app.route('/create_product',methods=['POST','GET'])
def create_product():
    with getcursorTO() as cur:
        if request.method == 'POST':
            # id = request.form['uuid']
            name = request.form['name']
            description = request.form['description']
            price = request.form['price']
            stock_quantity = request.form['stock_quantity']
            sql = """INSERT INTO products(name,description,price,stock_quantity)
                    VALUES (%s,%s,%s,%s);"""
            cur.execute(sql, (name,description,price,stock_quantity))
            flash('success')
    return redirect( url_for('add_product'))
@app.route('/delete_product/<int:id>')
def delete_product(id):
    with getcursorTO() as cur:
        sql = """DELETE FROM products WHERE id = %s;"""
        cur.execute(sql, (id,))
    return redirect(url_for('product'))
@app.route('/edit_product/<int:id>',methods=['post'])
def edit_product(id):
    with getcursorTO() as cur:
            id = request.form['id']
            name = request.form['name']
            description = request.form['description']
            price = request.form['price']
            stock_quantity = request.form['stock_quantity']
            sql = """UPDATE products SET name = %s,description = %s,price = %s,stock_quantity = %s WHERE id = %s;""" 	
            cur.execute(sql,(name,description,price,stock_quantity,id))
    return redirect(url_for('product'))


from flask import Flask, render_template, request, redirect, url_for, session, flash,send_from_directory
from app import app

@app.route('/dashborad')
def dashborad():
    pass
    return render_template('backend/dashborad.html')
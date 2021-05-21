import re
from flask import render_template, redirect, request, session
from flask.helpers import flash
from flask_app import app

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.email import Email


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submitEmail():
    if not Email.validate_email(request.form):
        return redirect('/')

    data = {
        'email_address': (request.form ['email_address']),
    }
    Email.saveToDB(data)
    flash('Thanks for entering a valid email address!')
    return redirect('/emailsMade')

@app.route("/emailsMade")
def showEmails():

    return render_template('indexEmailsMade.html', allEmails = Email.showEmailsInDB())
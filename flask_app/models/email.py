from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email_address']


    @classmethod
    def saveToDB(cls,data):
        query = 'INSERT INTO emails (email_address) VALUES(%(email_address)s);'
        return connectToMySQL('emailSchema').query_db(query, data)


    @staticmethod
    def validate_email(data):
        isValid = True
        if not EMAIL_REGEX.match(data['email_address']):
            flash("Invalid email address!")
            isValid = False
        return isValid

    @classmethod
    def showEmailsInDB(cls):
        query = 'SELECT email_address from emails;'
        return connectToMySQL('emailSchema').query_db(query)
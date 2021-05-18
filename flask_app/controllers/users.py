from flask import render_template, redirect, request, session
from flask_app import app

from flask_app.config.mysqlconnection import connectToMySQL




@app.route("/users")
def index():
    mysql = connectToMySQL('users_schema')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template("index.html", allUsers = users)
            
@app.route('/users/new')
def newUser():
    return render_template('indexCreate.html')

@app.route('/users/add', methods = ['POST'])
def indexCreate():
    print(request.form)
    query = 'INSERT INTO users(firstName, lastName, email, createdAt, updatedAt)VALUES(%(fname)s, %(lname)s, %(email)s, NOW(), NOW());'
    data = {
        "fname":request.form['first_name'],
        "lname":request.form['last_name'],
        "email":request.form['email'],
    }
    mysql = connectToMySQL('users_schema')
    id = mysql.query_db(query, data)
    return redirect(f'/users/{id}')

@app.route('/users/<id>')
def viewUser(id):
    query = 'SELECT * FROM users WHERE id = %(user_id)s;'
    data = {
        'user_id': int(id)
    }
    mysql = connectToMySQL('users_schema')
    user = mysql.query_db(query, data)
    return render_template('indexShow.html', user = user[0])
    


@app.route('/users/<id>/destroy')
def deleteUser(id):
    query = 'DELETE FROM users WHERE id = %(user_id)s;'
    data = {
        'user_id': int(id)        
    }
    
    mysql = connectToMySQL('users_schema')
    mysql.query_db(query, data)

    return redirect('/users')
    
@app.route('/users/<id>/edit')
def editUser(id):
    query = 'SELECT * FROM users WHERE id = %(user_id)s;'
    data = {
        'user_id': int(id)
    }
    mysql = connectToMySQL('users_schema')
    user = mysql.query_db(query, data)
    return render_template('indexEdit.html', user = user[0])
    

@app.route('/users/<id>/update', methods = ['POST'])
def indexEdit(id):
    print(request.form)
    query = 'UPDATE users SET firstName = %(fname)s, lastName = %(lname)s, email = %(email)s, updatedAt = NOW() WHERE id = %(userID)s;'
    data = {
        "userID": int(id),
        "fname":request.form['first_name'],
        "lname":request.form['last_name'],
        "email":request.form['email'],
    }
    mysql = connectToMySQL('users_schema')
    mysql.query_db(query, data)
    return redirect(f'/users/{id}')
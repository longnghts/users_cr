from flask import Flask, render_template, redirect, session, request, flash
from msqlConnection import connectToMySQL
app = Flask(__name__)
@app.route("/users")
def index():
    mysql = connectToMySQL('users_schema')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template("index.html", allUsers = users)
            
@app.route('/users/new')
def method_name():
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
    mysql.query_db(query, data)
    return redirect('/users')





if __name__ == "__main__":
    app.run(debug=True)

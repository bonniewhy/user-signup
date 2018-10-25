from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def user_form():
    encoded_error = request.args.get("error")
    return render_template('user_signup.html', error = encoded_error)

@app.route('/welcome', methods=['POST'])
def welcome_message():
    # Store all form data.
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    # Empty Field Error
    if username == "":
        error = "Please enter a username."
        return redirect("/?error=" + error)
    elif password == "":
        error = "Please enter a password."
        return redirect("/?error=" + error)
    elif verify == "":
        error = "Passwords must match."
        return redirect("/?error=" + error)

    # Username and Password Valid

    # Passwords Matching

    # Valid Email

    return render_template('welcome.html', username = username, password = password, verify = verify, email = email)

app.run()
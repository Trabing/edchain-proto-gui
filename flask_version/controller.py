#!/usr/bin/env python3

import sqlite3

from flask import Flask, g, redirect, render_template, request, session, url_for


connection = sqlite3.connect('master.db', check_same_thread=False)
cursor     = connection.cursor()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'swordfish'

@app.route('/')
def show_login():
    return render_template('login.html')

@app.route('/check-login', methods=["POST"])
def check_login():
    message = None
    submitted_username = request.form.get('username')
    submitted_password = request.form.get('password')
    objectified_username = cursor.execute('SELECT username FROM users WHERE username="{}";'.format(str(submitted_username))).fetchall()[0][0]
    objectified_password = cursor.execute('SELECT password FROM users WHERE username="{}";'.format(str(submitted_username))).fetchall()[0][0]
    if objectified_username:
        if submitted_password == objectified_password:
            return render_template('dashboard.html')
        else:
            message = "Access denied."
            return render_template('login.html', error_message=message)
    else:
        message = "Access denied."
        return render_template('login.html', error_message=message)

@app.route('/search')
def show_search():
    return render_template('search.html')

@app.route('/library')
def show_library():
    return render_template('library.html')

@app.route('/settings')
def show_settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)

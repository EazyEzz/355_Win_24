# Queens College
# Internet and Web Technology (CSCI 355)
# Winter 2024
# Assignment 11  - Web-Based Application
# Essmer Sanchez
# Collaboration: Worked With Class
from urllib import request
from flask import Flask, render_template, request, redirect, url_for, session
import webbrowser
import os

app = Flask(__name__)
logged_in = False


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'


@app.route('/states')
def states():
    title = "The United States of America"
    headers, data = read_file("states.csv")
    return render_template('results.html', title=title, headers=headers, data=data)


@app.route('/my_state', methods=['GET', 'POST'])
def my_state():
    if request.method.upper() == 'POST':
        state = request.form['state']
        title = "The United States of America"
        headers, data = read_file("states.csv")
        headers.append("selected")
        for row in data:
            row.append("")
            if row[0] == state:
                row[4] = '##########'
    return render_template('results.html', title=title, headers=headers, data=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in
    if request.method.upper() == 'GET':
        login = request.args.get('login')
        password = request.args.get('password')
    elif request.method.upper() == 'POST':
        login = request.form['login']
        password = request.form['password']
    if login == 'Essmer' and password == '355':
        logged_in = True
        headers, data = read_file("states.csv")
        states = [row[0] for row in data]
        #return f'User {login} has successfully logged in!'
        return render_template('choose_state.html', states=states)
    else:
        return f'User {login} has been rejected!'


def read_file(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        states = [line.strip().split(',') for line in lines]
        return states[0],states[1:]


def open_file_in_browser(file_name):
    url = 'file:///' + os.getcwd() + '/' + file_name
    print(url)
    webbrowser.open_new_tab(url)


if __name__ == '__main__':
    app.run()
    # app.open_file_in_browser('templates/login.html')

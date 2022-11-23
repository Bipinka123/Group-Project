import json
import flask
from dotenv import load_dotenv, find_dotenv
import os
import random
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, request, flash
from flask_login import login_user, login_required, UserMixin, login_manager, LoginManager, logout_user




load_dotenv(find_dotenv())

app = flask.Flask(__name__)

app.secret_key = 'groupproject'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader

def load_user(user_id):
        return Persons.query.get(int(user_id))


class Persons(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

with app.app_context():
    db.create_all()

@app.route('/')
def signupPage():
    return flask.render_template('signup.html')

@app.route('/signup' , methods = ['GET', 'POST'])
def handleSignup():
    
    
    user_name = request.form.get('Username')
    newUser = Persons(username = user_name)

    user = Persons.query.filter_by(username = user_name).first()

    if user:
        flash("Username exists. Please enter different user or click login")
        return redirect(url_for('signupPage'))

    db.session.add(newUser)
    db.session.commit()

    return redirect(url_for('loginPage'))


@app.route('/login')
def loginPage():
    return flask.render_template('login.html')


@app.route('/login', methods = ['GET', 'POST'])
def handleLogin():

    user_name = request.form.get('Username')
    
    checkUser = Persons.query.filter_by(username = user_name).first()

    if not checkUser:
        flash("Username does not exist. Please signup or try again!")
        return redirect(url_for('loginPage'))
    
    else:
        login_user(checkUser)
        return redirect(url_for('mainPage'))

    
@login_required
@app.route('/main', methods = ['GET', 'POST'])
def mainPage():
    return flask.render_template('main.html')


@login_required
@app.route('/logout', methods = ['GET', 'POST'])
def handleLogout():
    logout_user()
    return redirect(url_for('loginPage'))


app.run(debug=True)



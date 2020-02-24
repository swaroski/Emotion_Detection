
#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from __future__ import division
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import cryptography
from datetime import datetime

from flask import Flask, render_template
#from __future__ import division
import numpy as np
import pandas as pd
import time

import utils
#from utils.utils import *

import re
import os
from collections import Counter
import altair as alt
from jinja2 import *

### Flask imports
import requests
from flask import Flask, render_template, session, request, redirect, flash, Response
## filename generator
import uuid

from flask_cors import CORS
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '.\\upload_files'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    date_created = db.Column(db.DateTime, default= datetime.now)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

    

@app.route('/')
def index():
    loginform = LoginForm()
    registerform = RegisterForm()
    return render_template('signlog.html', loginform = loginform, registerform=registerform )

@app.route('/login', methods=['POST'])
def login():
    loginform = LoginForm()
    registerform = RegisterForm()
    if loginform.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('index.html', loginform = loginform, registerform=registerform)

@app.route('/signup', methods=['POST'])
def signup():
    registerform = RegisterForm()
    loginform = LoginForm()
    if registerform.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signlog.html', registerform=registerform, loginform = loginform)

@app.route('/review', methods=['POST'])
@login_required
def dashboard():
    return render_template('index1.html', name=current_user.username)

@app.route('/uploads', methods=["POST"])
def upload():
    if request.method == 'POST':
        print(request.headers)
        file = request.files['video-blob']
        filename = str(uuid.uuid4().hex) + ".webm"
        filename = secure_filename(filename)
        
        file.save(os.path.join(UPLOAD_FOLDER, filename))
    return "success"



    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
   

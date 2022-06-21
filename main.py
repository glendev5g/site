import os
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user
from app import app, db
from app.models import User

INPUT_FOLDER = os.path.join(os.getcwd(),'uploads')


@app.route('/')
def homepage():
    return render_template('index.html')

"""================"""

"""LOGIN AND REGISTER"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        pwd = request.form['password']

        user = User(name, username, pwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        pwd = request.form['password']

        user = User.query.filter_by(email=name).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

"""================"""

""" UPLOAD SCREEN """

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['imagem']
    savPath = os.path.join(INPUT_FOLDER, secure_filename(file.filename))
    file.save(savPath)
    return render_template('upload.html')

@app.route('/apps')
def apps():
    return render_template('apps.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

if __name__=="__main__":
    app.run(debug=True)
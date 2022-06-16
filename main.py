from flask import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

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

@app.route('/register')
def register():
    return render_template('register.html')


if __name__=="__main__":
    app.run(debug=True)
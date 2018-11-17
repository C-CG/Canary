from flask import Flask, render_template
from canary import Tokenizer
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/tokenizer')
def tokenizer():
    return Tokenizer('Hello - Canary')

@app.errorhandler(404)
def error_404(error):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
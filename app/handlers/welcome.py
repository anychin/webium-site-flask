from flask import render_template
from ..app import app

@app.route('/')
def welcome():
    return render_template('welcome/welcome.html')

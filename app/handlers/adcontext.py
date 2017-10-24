from flask import render_template
from ..app import app

@app.route('/ad-context')
def show_landing_adcontext():
    return render_template('landing/ad-context.html')

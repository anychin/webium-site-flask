from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_assets import Environment
from flask_assets import Bundle

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/ad-context')
def show_landing_adcontext():
    return render_template('landing/ad-context.html')

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)

@app.route('/')
def welcome():
    return render_template('welcome/welcome.html')

# compile assets
assets = Environment(app)
assets.url = app.static_url_path

css_bundle = Bundle('css/application.sass', 'css/landing.sass', filters='sass', output='all.css')
assets.register('css_all', css_bundle)

if __name__ == "__main__":
    app.run()

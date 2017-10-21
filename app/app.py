from flask import Flask, render_template, request, redirect, url_for
from flask_assets import Environment, Bundle


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome/welcome.html')

@app.route('/ad-context')
def show_landing_adcontext():
    return render_template('landing/ad-context.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# compile assets
assets = Environment(app)
assets.url = app.static_url_path

css_bundle = Bundle('css/application.sass', filters='sass', output='all.css')
assets.register('css_all', css_bundle)

if __name__ == "__main__":
    app.run()

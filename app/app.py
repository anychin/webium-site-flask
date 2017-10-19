from flask import Flask, render_template, request, redirect, url_for
from flask_assets import Environment, Bundle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome/welcome.html')

# compile assets
assets = Environment(app)
assets.url = app.static_url_path

css_bundle = Bundle('css/application.sass', filters='sass', output='all.css')
assets.register('css_all', css_bundle)

if __name__ == "__main__":
    app.run()    

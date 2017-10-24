from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_assets import Environment
from flask_assets import Bundle

app = Flask(__name__)

from . import handlers

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

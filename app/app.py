from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_assets import Environment
from flask_assets import Bundle
import requests
import logging

app = Flask(__name__)
app.config.from_object('config')

@app.route('/ad-context', methods=['GET', 'POST'])
def show_landing_adcontext():
    error = None
    if request.method == 'POST':
        to = "hello@webiumdigital.com"
        phone = request.form['phone']
        website = request.form['website']
        text = 'Phone: {}, Site: {}\n\n'.format(phone, website)
        send_email(to, text)
    return render_template('landing/ad-context.html', error=error)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)

@app.route('/')
def welcome():
    return render_template('welcome/welcome.html')

# [START simple_message]
def send_email(to, text):
    url = 'https://api.mailgun.net/v3/{}/messages'.format(app.config['MAILGUN_DOMAIN_NAME'])
    auth = ('api', app.config['MAILGUN_API_KEY'])
    text = text + request.headers.get('User-Agent')
    data = {
        'from': 'Webium Page <mailgun@{}>'.format(app.config['MAILGUN_DOMAIN_NAME']),
        'to': to,
        'subject': 'Request from a website',
        'text': text,
    }
    requests.post(url, auth=auth, data=data)
# [END simple_message]

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

# compile assets
assets = Environment(app)
assets.url = app.static_url_path

css_bundle = Bundle('css/application.sass', 'css/landing.sass', filters='sass', output='all.css')
assets.register('css_all', css_bundle)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

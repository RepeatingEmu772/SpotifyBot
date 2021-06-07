import flask
from flask import url_for, jsonify, make_response

import SpotifyOAuth

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template("index.html")

@app.route('/login')
def accessSpotify():
    response = SpotifyOAuth.RedirectTologin(redirect_uri='https://localhost:7001/authorized')
    return flask.redirect(url_for('SP_redirect_uri'))

@app.route('/authorized')
def SP_redirect_uri():
    print("spotify connected")
    return "spotify connected"

def main():
    print("nothin")

if __name__ == '__main__':
    app.run(use_reloader=True,port=7001)

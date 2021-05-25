from flask import Flask, render_template, request, session, redirect, url_for
import spotipy
import pandas as pd
import json
import time

app = Flask(__name__)

app.secret_key = "newfonWNFEIN"
app.config['SESSION_COOKIE_NAME'] = 'bear'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
    return 'now logged in'

@app.route('/function')
def functions():
    return 'thank fuckin god'

client_id='0e14f5cb72ab42c8ba685b2f853ce397'
client_secret='265efd1824764479a4e6866d33b8b483'

def create_spotify_oauth():
    return spotipy.oauth2.SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=url_for('redirectPage', _external=True),
        scope='user-library-read'
    )
from flask import jsonify, make_response
import requests
import json
import shutil
import os

def RedirectTologin(redirect_uri="https://localhost:7001/authorized"):
    token_uri="https://accounts.spotify.com/authorize"
    method="GET"
    params={
        "client_id" : '0e14f5cb72ab42c8ba685b2f853ce397',
        "response_type" : 'code',
        "redirect_uri" : redirect_uri,
        "scope" : 'user-read-email'
    }
    client_secret='265efd1824764479a4e6866d33b8b483'
    r = requests.get(token_uri,params=params)
    print(r)
    #return make_response(r,200)

if __name__=='__main__':
    RedirectTologin()
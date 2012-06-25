from gdomain import Domain
from hackparty import app

from google.appengine.api import memcache

from flask import render_template, request
import json

@app.route('/')
def hello_world():
    return render_template('helloworld.html')

@app.route('/users')
def users():
    d = Domain("hackparty.org", "jeff.lindsay@hackparty.org", memcache.get("domain_pass"))
    return json.dumps(d.email.get_forwarding('jeff.lindsay'))

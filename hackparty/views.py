from gdomain import Domain
from hackparty import app

from google.appengine.api import memcache

from flask import render_template, request
import json

@app.route('/preregistration', methods=['GET', 'POST'])
def preregistration():
    if request.method == 'GET':
        return render_template('preregistration.html')
    if request.method == 'POST':
        return render_template('helloworld.html')

@app.route('/complete_register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        return render_template('helloworld.html')

@app.route('/')
def hello_world():
    return render_template('helloworld.html')

@app.route('/users')
def users():
    d = Domain("hackparty.org", "jeff.lindsay@hackparty.org", memcache.get("domain_pass"))
    return json.dumps(d.groups.all())

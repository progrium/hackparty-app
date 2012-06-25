from application import app
from flask import render_template, request

@app.route('/')
def hello_world():
    return render_template('helloworld.html')
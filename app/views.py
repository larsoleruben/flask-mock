from app import app
from flask import jsonify
from flask import render_template

@app.route('/')
def home():
   return "hello world, from Lars!"

@app.route('/ccev')
def ccev():
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@app.route('/template')
def template():
    return render_template('home.html')
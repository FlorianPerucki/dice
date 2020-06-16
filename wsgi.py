# wsgi.py
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
	return jsonify({ 'error': "Head over to /roll" }) 

@app.route('/roll')
def roll():
	return jsonify({ 'roll': 0 }) 
# wsgi.py
from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/')
def home():
	return jsonify({ 'error': "Head over to /roll" }) 

@app.route('/roll')
def roll():
	return jsonify({ 'roll': random.randint(1, 6), "testing": True })

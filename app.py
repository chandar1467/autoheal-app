from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Auto-Healing App Running!"

@app.route('/crash')
def crash():
    os._exit(1)

app.run(host='0.0.0.0', port=5000)

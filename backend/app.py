from flask import Flask, request, render_template, url_for
import os
import time
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/exchange')
def exchange():
    return render_template('get_photo.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

from flask import Flask, request, render_template, url_for
import os
import time
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('.html')

@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    img_src = url_for('static', filename = 'uploads/' + filename)
    


    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

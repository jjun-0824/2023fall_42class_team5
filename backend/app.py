from flask import Flask, request, render_template, url_for
import os
import time
import sys

app = Flask(__name__)

@app.route('/')
def index():
    # 기본적으로 이 index 함수가 실행됨.
    return render_template('home.html')

@app.route('/link')
def get_link():
    link="https://1234"
    # 전달해주고 싶은 결과값을 html내에서 변경해주고 싶을 때 하단과 같은 방법으로 변환
    return render_template('home.html', url=link) # 넘겨주고 싶은 변수 옆에 적어넣기

@app.route('/upload', methods = ['POST'])
def upload():
    file= request.files['file'] # 사진이나 입력값은 request로 받기
    filename = file.filename
    filepath=os.path.join('static/uploads', filename)
    file.save(filepath)

    return render_template('get_photo_a.html',image=filepath)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

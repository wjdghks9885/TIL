from flask import Flask
from flask import render_template
from flask import request
import random
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/mulcam')
def mulcam():
    return "This is mulcam!"

@app.route('/greeting/<string:name>')
def greeting(name):
    return f"Hello, {name}"

@app.route("/cube/<int:num>")
def cube(num):
    result = num ** 3
    return str(result)

@app.route("/lunch/<int:people>")
def lunch(people):
    menu = ['짜장면', '짬뽕', '볶음밥', '잡채밥', '제육볶음', '짬뽕밥', '꽝']
    order = random.sample(menu, people)
    return str(order)

@app.route("/html")
def html():
    return '<h1>안녕하세요!!!</h1>'

@app.route('/html_file')
def html_file():
    return render_template('html_file.html')

@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', your_name=name)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('pong.html', name=name, message=message)

@app.route('/sin')
def sin():
    return render_template('sin.html')

@app.route('/sin_result')
def sin_result():
    name = request.args.get('name')
    w1 = ["미모", "기럭지", "키", "잘생김", "멍청함", "살", "똑똑함", "못생김"]
    word = random.sample(w1, 2)
    word1 = word[0]
    word2 = word[1]
    return render_template('sin_result.html', name=name, word1=word1, word2=word2)

@app.route('/ascii')
def ascii():
    return render_template('ascii.html')

@app.route('/ascii_result')
def ascii_result():
    # 1. form 태그로 날린 데이터를 받는다.
    word = request.args.get('word')

    # 2. word를 가지고 ascii_art API 요청 주소로 요청을 보낸다.
    result = requests.get(f"http://artii.herokuapp.com/make?text={word}").text
    
    # 3. API 응답 결과를 html 파일에 담아서 보여준다.
    return render_template('ascii_result.html', result=result)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    numbers = request.args.get('numbers')  # string
    numbers = numbers.split()  # list
    numbers_int = []
    for n in numbers:
        numbers_int.append(int(n))

    res = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}')
    lotto = res.json()

    winner = []
    # 1. for문을 활용한다.
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    # # 2. List Comprehension
    # winner = [lotto[f'drwtNo{i}' for i in range(1, 7)]]
    # # drwtNo6 = lotto.get("drwtNo6")  # .get으로 가져와야 없을 때 에러 안나고 None이 반환 됨
    
    matched = len(set(winner) & set(numbers_int))
    if matched == 6:
        result = '1등입니다!!!'
    elif matched == 5:
        if lotto["bnusNo"] in numbers_int:
            result = '2등입니다!!'
        else:
            result = '3등입니다!'
    elif matched == 4:
        result = '4등입니다..'
    elif matched == 3:
        result = '5등입니다...'
    else:
        result = '꽝입니다.......'

    return render_template('lotto_result.html',
        lotto_round=lotto_round,
        winner=winner,
        numbers_int=numbers_int,
        result=result)

if __name__ == "__main__":
    app.run(debug = True)
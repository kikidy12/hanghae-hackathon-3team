from flask import Flask, render_template, jsonify, session, redirect, url_for
from user import *
from bookManage import *
from book import *
from comment import *

# JWT 토큰을 만들 때 필요한 비밀문자열입니다. 아무거나 입력해도 괜찮습니다.
# 이 문자열은 서버만 알고있기 때문에, 내 서버에서만 토큰을 인코딩(=만들기)/디코딩(=풀기) 할 수 있습니다.
SECRET_KEY = 'SPARTA'

# JWT 패키지를 사용합니다. (설치해야할 패키지 이름: PyJWT)
import jwt

# 토큰에 만료시간을 줘야하기 때문에, datetime 모듈도 사용합니다.
import datetime

# 회원가입 시엔, 비밀번호를 암호화하여 DB에 저장해두는 게 좋습니다.
# 그렇지 않으면, 개발자(=나)가 회원들의 비밀번호를 볼 수 있으니까요.^^;
import hashlib


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/book')
def apiBookList():
    test = getBookList()
    return test


@app.route('/register')
def register():
    return render_template('signUp.html')

@app.route('/login')
def logIn():
    return render_template('signIn.html')


@app.route('/api/register', methods=['POST'])
def apiRegister():
    giveUserInfo = apiRegester()
    return giveUserInfo

@app.route('/api/login', methods = ['POST'])
def apiLogin():
    logIn = apiLogin()
    return logIn

@app.route('/api/nickName', methods = ['GET'])
def apiValid():
    checkUp = apiValid()
    return checkUp

if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)

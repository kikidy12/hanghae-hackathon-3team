from flask import Flask, render_template, jsonify, session, redirect, url_for
from user import *
from bookManage import *
from book import *
from comment import *
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
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        return render_template('index.html', nickname=user_info["nick"])
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/api/book')
def apiBookList():
    test = getBookList()
    return test


@app.route('/register')
def register():
    return render_template('signUp.html')

@app.route('/logIn')
def logIn():
    return render_template('signIn.html')


@app.route('/api/register', methods=['POST'])
def apiRegister():
    giveUserInfo = apiRegester()
    return giveUserInfo

@app.route('/api/login', methods = ['POST'])
def apiLogIn():
    logIn = apiLogin()
    return logIn

@app.route('/api/nickName', methods = ['GET'])
def apiValid():
    checkUp = apiValid()
    return checkUp

if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)

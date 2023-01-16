from flask import Flask, render_template, jsonify, session, redirect, url_for
from user import *
from bookManage import *
from book import getBook, getBookList
from comment import addComment, addSubComment, getCommentList, deleteComment
from favorite import addBookLikePlus

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
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        return render_template('index.html', nickname=user_info["nick"])
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

@app.route('/api/bookdetail')
def apiGetBook():
  json = getBook()
  return json


@app.route('/api/bookLikePlus', methods=["POST"])
def apiPostBookLikePlus():
  message = addBookLikePlus()
  return message

@app.route('/api/booklist')
def apiGetBookList():
  json = getBookList()
  return json

@app.route('/api/commentlist', methods=["GET"])
def apiGetCommentList():
  json = getCommentList()
  return json


@app.route('/api/comment', methods=["POST"])
def apiPostComment():
  message = addComment()
  return message


@app.route('/api/subcomment', methods=["POST"])
def apiPostSubComment():
  message = addSubComment()
  return message



@app.route('/api/comment', methods=["DELETE"])
def apiDeleteComment():
  message = deleteComment()
  return message
  

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

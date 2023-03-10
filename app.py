from flask import Flask, render_template, jsonify, session, redirect, url_for
from bookManage import *
from book import getBook, getBookList
from comment import addComment, addSubComment, getCommentList, deleteComment
from favorite import addBookLikePlus
from dislike import addBookDisLikePlus

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

@app.route('/detailBooks')
def detailBooks():
  return render_template('detailBooks.html')

@app.route('/api/book/register', methods=["POST"])
def apiBookPOST():
    testBook = registerBook()
    return testBook

@app.route('/api/book/modify', methods=["POST"])
def apiModifyBookPOST():
  testBook = modifyBook()
  return testBook

# api
@app.route('/api/book/detail')
def apiGetBook():
  json = getBook()
  return json

@app.route('/api/book/like/plus', methods=["POST"])
def apiPostBookLikePlus():
  message = addBookLikePlus()
  return message

  
#닉네임 중복체크
@app.route('/ninkcheck', methods=['POST'])
def nink_check():
    nickNameReceive = request.form['nickNameGive']
    ninkcheck = db.user.find_one({'userNickName': nickNameReceive}, {'_id': False})
    print(ninkcheck)
    if ninkcheck is None:
        nink_duplicate_check = True
        return jsonify({'msg': '사용가능️', 'nink_duplicate_check': nink_duplicate_check})
    else:
        ninkcheck = ninkcheck['userNickName']
        if ninkcheck == nickNameReceive:
            nink_duplicate_check = False
            return jsonify({'msg': '사용불가', 'nink_duplicate_check': nink_duplicate_check})

# 아이디 중복확인
@app.route('/idcheck', methods=['POST'])
def id_check():
    idReceive = request.form['idGive']
    idcheck = db.user.find_one({'userId': idReceive}, {'_id': False})
    print(idcheck)

    if idcheck is None:
        id_duplicate_check = True
        return jsonify({'msg': '사용가능️', 'id_duplicate_check': id_duplicate_check})
    else:
        idcheck = idcheck['userId']
        if idcheck == idReceive:
            id_duplicate_check = False
            return jsonify({'msg': '사용불가', 'id_duplicate_check': id_duplicate_check})


@app.route('/api/book/dislike/plus', methods=["POST"])
def apiPost():
  message = addBookDisLikePlus()
  return message
@app.route('/api/register', methods=['POST'])
def apiRegister():
    idReceive = request.form['idGive']
    pwReceive = request.form['pwGive']
    nickNameReceive = request.form['nickNameGive']
    userList = list(db.user.find({}, {'_id':False}))
    userNum = len(userList) + 1

    pwHash= hashlib.sha256(pwReceive.encode('utf-8')).hexdigest()

    doc = {
        'userNumber':userNum,
        'userId':idReceive,
        'userNickName':nickNameReceive,
        'userPassword':pwHash
    }

    db.user.insert_one(doc)
    return jsonify({'result':'success'})




@app.route('/api/login', methods = ['POST'])
def apiLogin():
    idReceive = request.form['idGive']
    pwReceive = request.form['pwGive']
    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pwHash = hashlib.sha256(pwReceive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
    result = db.user.find_one({'userId': idReceive, 'userPassword': pwHash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'userId': idReceive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5000)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

# [유저 정보 확인 API]
# 로그인된 유저만 call 할 수 있는 API입니다.
# 유효한 토큰을 줘야 올바른 결과를 얻어갈 수 있습니다.
# (그렇지 않으면 남의 장바구니라든가, 정보를 누구나 볼 수 있겠죠?)
@app.route('/api/valid', methods = ['GET'])
def apiValid():
    tokenReceive = request.cookies.get('mytoken')

    # try / catch 문?
    # try 아래를 실행했다가, 에러가 있으면 except 구분으로 가란 얘기입니다.

    try:
        # token을 시크릿키로 디코딩합니다.
        # 보실 수 있도록 payload를 print 해두었습니다. 우리가 로그인 시 넣은 그 payload와 같은 것이 나옵니다.
        payload = jwt.decode(tokenReceive, SECRET_KEY, algorithms=['HS256'])
        

        # payload 안에 id가 들어있습니다. 이 id로 유저정보를 찾습니다.
        # 여기에선 그 예로 닉네임을 보내주겠습니다.
        userinfo = db.user.find_one({'userId': payload['userId']}, {'_id': 0})

        return jsonify({'result': 'success', 'nickname': userinfo['userNickName']})
    # except jwt.ExpiredSignatureError:
    #     # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
    #     return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})
@app.route('/api/book/list')
def apiGetBookList():
  json = getBookList()
  return json

@app.route('/api/comment/list', methods=["GET"])
def apiGetCommentList():
  json = getCommentList()
  return json


@app.route('/api/comment', methods=["POST"])
def apiPostComment():
  message = addComment()
  return message


@app.route('/api/comment/sub', methods=["POST"])
def apiPostSubComment():
  message = addSubComment()
  return message

@app.route('/api/comment', methods=["DELETE"])
def apiDeleteComment():
  message = deleteComment()
  return message


if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)

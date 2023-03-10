from flask import Flask, request, render_template, jsonify, session, redirect, url_for
from db import db
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


# jwt 토큰 검증으로 user정보 처리
def checkToken():
    try:
        token_receive = request.cookies.get('mytoken')
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        userInfo = db.user.find_one({"userId": payload['userId']})
        return userInfo
    # except jwt.ExpiredSignatureError:
    # 토큰 오류시 error발생
    except jwt.exceptions.DecodeError:
        raise Exception('토큰 오류')
    # 기타 에러 발생시 에러 raise
    except Exception as e:
        raise e
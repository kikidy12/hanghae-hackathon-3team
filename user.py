from db import db
from flask import jsonify, request

import jwt

def apiRegester():
    idReceive = request.form['idGive']
    pwReceive = request.form['pwGive']
    nickNameReceive = request.form['nickNameGive']
    userNum = len(userList)+1
    userList = list(db.user.find({}, {'_id':False}))

    pwHash= hashlib.sha256(pwReceive.encode('utf-8')).hexdigest()

    doc = {
        'userNumber':userNum,
        'userId':idReceive,
        'userNickName':nickNameReceive,
        'userPassword':pwHash
    }

    db.user.insert_one(doc)
from db import db
from flask import jsonify, request


# 좋아요 추가
def addBookDisLikePlus():
  bookId = int(request.form['bookId'])

  book = db.book.find_one({'id': bookId}, {'_id': False})
  db.book.update_one({"id":bookId},{"$set":{"disLikeCount":int(book['disLikeCount']) + 1}})

  return jsonify({'message':'좋아요 추가완료'})
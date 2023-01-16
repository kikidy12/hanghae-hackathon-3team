from db import db
from flask import jsonify, request


# 좋아요 추가
def addBookLikePlus():
  bookId = int(request.form['bookId'])

  book = db.book.find_one({'id': bookId}, {'_id': False})

  db.book.update_one({"id":bookId},{"$set":{"likeCount":(int(book['likeCount']) + 1)}})

  return jsonify({'result': 'success', 'message':'좋아요 추가완료'})
from db import db
from flask import jsonify, request


# 댓글 목록 조회
def getCommentList():
  commentList = list(db.comment.find({}, {'_id': False}))
  return jsonify({'commentList':commentList})


# 댓글 등록
def addComment():
  userId = int(request.form['uesrId']);
  bookId = int(request.form['bookId']);
  comment = request.form['comment'];

  # 커맨트 id순으로 정렬
  commentList = list(db.comment.find({}, {'_id': False}).sort('id'))

  # 마지막 번호를 호출한다
  lastId = commentList[-1]['id'] if len(commentList) > 0 else 1

  comment = db.comment.insert_one({'id': lastId, 'userId': userId, 'bookId': bookId, 'comment': comment, 'isSub': False })

  return jsonify({'message':'등록완료'})


# 대댓글 등록
def addSubComment():
  userId = int(request.form['uesrId']);
  bookId = int(request.form['bookId']);
  commentId = int(request.form['commentId']);
  comment = request.form['comment'];

  # 장소목록을 num순으로 정렬
  comment_list = list(db.comment.find({}, {'_id': False}).sort('id'))

  # 마지막 번호를 호출한다
  lastId = comment_list[-1]['id'] if len(comment_list) > 0 else 1

  comment = db.comment.insert_one({'id': lastId, 'userId': userId, 'bookId': bookId, 'commentId': commentId, 'comment': comment, 'isSub': True })

  return jsonify({'message':'등록완료'})



# 댓글 삭제 (삭제시 하위에 달려있는 댓글까지 모두 삭제)
def deleteComment():
  userId = int(request.form['uesrId']);
  commentId = int(request.form['commentId']);
  
  db.comment.delete_one({"id":commentId, 'userId': userId})
  db.comment.delete({"commentId":commentId})

  return jsonify({'message':'삭제완료'})
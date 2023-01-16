
from db import db
from flask import jsonify, request


# 책 상세 조회 (댓글 목록까지 추가)
def getBook():
  bookId = int(request.args.get('bookId'))

  bookList = db.book.aggregate([
      {
          # sql의 join기능을 수행
          '$lookup': {
              'from': "comment",
              'localField': "comment.bookId",
              'foreignField': "book.id",
              'as': "comment",
          },
      },
      {
          # 요청한 bookId를 기준삼아 진행한다
          '$match': {'id': bookId}
      },
      {
          # 노출시키지 않을 컬럼을 제거시켜준다
          '$unset': ["_id", 'comment._id']
      },
  ])

  bookList = list(bookList)

  book = bookList[0] if len(bookList) > 0 else None

  return jsonify({'book':book})


# 책 목록 조회
def getBookList():
  bookList = list(db.book.find({}, {'_id': False}))
  return jsonify({"bookList": bookList})


# 책 등록 조회
def addBook():
  bookList = list(db.book.find({}, {'_id': False}))
  print('book')
  return jsonify(bookList)
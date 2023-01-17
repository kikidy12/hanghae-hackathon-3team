
from db import db
from flask import jsonify, request


# 책 상세 조회 (댓글 목록까지 추가)
def getBook():
  try:
    bookId = int(request.args.get('bookId'))

    book = db.book.find_one({'id': bookId}, {'_id': False})

    commentList = db.comment.aggregate([
        {
            # sql의 join기능을 수행
            '$lookup': {
                'from': "user",
                'localField': "userId",
                'foreignField': "userNumber",
                'as': "user",
            },
        },
        {
            # 요청한 bookId를 기준삼아 진행한다
            '$match': {'bookId': bookId}
        },
        {
          '$unwind': {'path':'$user'}
        },
        {
            # 노출시키지 않을 컬럼을 제거시켜준다
            '$unset': ["_id", 'user._id']
        },
    ])

    book['comment'] = list(commentList)
  
    return jsonify({'result': 'success', 'book': book})

  except:
    return jsonify({'result': 'fail', 'message': '조회 실패'})


# 책 목록 조회
def getBookList():
  try:
    bookList = list(db.book.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'bookList': bookList})
  except:
    return jsonify({'result': 'fail', 'message': '조회 실패'})
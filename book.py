from db import db
from flask import jsonify, request


def getBookList():
  bookList = list(db.book.find({}, {'_id': False}))
  return jsonify(bookList)
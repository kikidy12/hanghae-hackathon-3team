
from flask import Flask, request, render_template, jsonify, session, redirect, url_for
from user import *
from bookManage import *
from book import getBook, getBookList
from comment import addComment, addSubComment, getCommentList, deleteComment
from favorite import addBookLikePlus
from dislike import addBookDisLikePlus


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

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

@app.route('/api/book/dislike/plus', methods=["POST"])
def apiPost():
  message = addBookDisLikePlus()
  return message


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


@app.route('/api/omment/sub', methods=["POST"])
def apiPostSubComment():
  message = addSubComment()
  return message

@app.route('/api/comment', methods=["DELETE"])
def apiDeleteComment():
  message = deleteComment()
  return message


if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)

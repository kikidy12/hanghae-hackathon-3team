
from flask import Flask, render_template, jsonify, session
from user import *
from bookManage import *
from book import getBook, getBookList
from comment import addComment, addSubComment, getCommentList, deleteComment
from favorite import addBookLikePlus

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/bookdetail')
def apiGetBook():
  json = getBook()
  return json


@app.route('/api/bookLikePlus', methods=["POST"])
def apiPostBookLikePlus():
  message = addBookLikePlus()
  return message

@app.route('/api/booklist')
def apiGetBookList():
  json = getBookList()
  return json

@app.route('/api/commentlist', methods=["GET"])
def apiGetCommentList():
  json = getCommentList()
  return json


@app.route('/api/comment', methods=["POST"])
def apiPostComment():
  message = addComment()
  return message


@app.route('/api/subcomment', methods=["POST"])
def apiPostSubComment():
  message = addSubComment()
  return message



@app.route('/api/comment', methods=["DELETE"])
def apiDeleteComment():
  message = deleteComment()
  return message
  

if __name__ == '__main__':
  app.run('0.0.0.0', port=5500, debug=True)
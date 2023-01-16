from flask import Flask, render_template, jsonify, session
from user import *
from bookManage import *
from book import *
from comment import *

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/api/book')
def apiBookList():
  test = getBookList()
  return test
  

if __name__ == '__main__':
  app.run('0.0.0.0', port=5500, debug=True)
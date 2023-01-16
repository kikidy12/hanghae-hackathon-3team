from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)


client = MongoClient('mongodb+srv://test:sparta@Cluster0.r0xf715.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signUp')
def signUp():
    return render_template('signUp.html')


@app.route('/signIn')
def signIn():
    return render_template('signIn.html')

@app.route('/detail')
def detail():
    return  render_template('detailBooks.html')


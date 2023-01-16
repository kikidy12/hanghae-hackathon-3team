from flask import Flask, render_template, request, jsonify
from db import db

def registerBook():
    bookTitleReceive = request.form['bookTitleGive']
    bookAuthorReceive = request.form['bookAuthorGive']
    bookThumbnailReceive = request.form['bookThumbnailGive']
    bookPublisherReceive = request.form['bookPublisherGive']
    bookSummaryReceive = request.form['bookSummaryGive']

    book_list = list(db.book.find({}, {'_id': False}).sort('id'))
    lastBookId = 1
    if len(book_list) > 0:
        lastBookId = book_list[-1]['id']
    else:
        lastBookId = 1

    doc = {
        'id':lastBookId+1,
        'bookTitle':bookTitleReceive,
        'bookAuthor':bookAuthorReceive,
        'bookThumbnail':bookThumbnailReceive,
        'bookPublisher':bookPublisherReceive,
        'bookSummary':bookSummaryReceive,
        'likeCount': 0,
        'dislikeCount': 0
    }

    db.book.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})

# def modifyBook():
#     idReceive = request.form['idGive']
#     bookDoc = db.book.find_one({'id': idReceive})
#
#     db.book.insert_one(bookDoc)
#
#     return jsonify(bookDoc)

def modifyBook():
    idReceive = request.form['bookIdGive']
    bookTitleReceive = request.form['bookTitleGive']
    bookAuthorReceive = request.form['bookAuthorGive']
    bookThumbnailReceive = request.form['bookThumbnailGive']
    bookPublisherReceive = request.form['bookPublisherGive']
    bookSummaryReceive = request.form['bookSummaryGive']


    doc = {
        'bookTitle':bookTitleReceive,
        'bookAuthor':bookAuthorReceive,
        'bookThumbnail':bookThumbnailReceive,
        'bookPublisher':bookPublisherReceive,
        'bookSummary':bookSummaryReceive
    }

    db.book.update_one({'id':int(idReceive)},{'$set':doc})

    return jsonify({'msg': '수정 완료!'})

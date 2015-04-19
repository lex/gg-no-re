# -*- coding: utf-8 -*-
from flask import (Flask,
        request,
        render_template,
        redirect,
        url_for)

from json import JSONEncoder

import json

from ming import (create_datastore,
        Session,
        collection,
        Field,
        Document,
        schema)

from bson.objectid import ObjectId

if __name__ == '__main__':
    bind = create_datastore('ggnore')
    session = Session(bind)
    app = Flask(__name__)
    app.config['STATIC_FOLDER'] = 'static'
else:
    bind = create_datastore('mim://localhost:27017', database='test')
    pass

BookModel = collection('reference_book',
        session,
        Field('_id', schema.ObjectId),
        Field('title', str),
        Field('author', str),
        Field('pages', str),
        Field('year', str),
        Field('publisher', str))

class Book:
    def __init__(self, title, author, pages, year, publisher, db_id):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        self.publisher = publisher
        self.db_id = db_id
        self.bibtex = """
@Book{{
    author = "{}",
    title = "{}",
    publisher = "{}",
    year = "{}",
}}
""".format(author, title, publisher, year)

class Inproceedings:
    def __init__(self, author, title, school, year, db_id):
        self.author = author
        self.title = title
        self.school = school
        self.year = year
        self.db_id = db_id
        self.bibtex = """
@INPROCEEDINGS{{
    author = "{}",
    title = "{}",
    school = "{}",
    year = "{}",
}}
""".format(author, title, school, year)


class Article:
    def __init__(self, author, title, journal, year, volume, db_id):
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.volume = volume
        self.db_id = db_id
        self.bibtex = """
@ARTICLE{{
    author = "{}",
    title = "{}",
    journal = "{}",
    year = "{}",
    volume = "{}",
}}
""".format(author, title, journal, year, volume)

class Enc(JSONEncoder):
    def default(self, o):
        return o.__dict__

@app.route('/')
def main():
    return render_template('index.html',
            books = list_books_as_json())

@app.route('/add_book', methods=['GET', 'POST'])
def book_adding():
    if request.method == 'GET':
        return render_template('add_book.html')
    else:
        r = request.form
        add_book(r['title'],
                r['author'],
                r['pages'],
                r['year'],
                r['publisher'])

        return redirect('/')

@app.route('/delete_book/<b_id>')
def book_deleting(b_id):
    BookModel.m.remove({'_id': ObjectId(b_id)})
    return redirect('/')

@app.route('/edit_book/<b_id>', methods=['GET', 'POST'])
def editing(b_id):
    if request.method == 'GET':
        b = get_book(b_id)
        return render_template('edit_book.html', book = Enc().encode(b))
    else:
        r = request.form
        edit_book(r['title'],
                r['author'],
                r['pages'],
                r['year'],
                r['publisher'],
                r['db_id'])

        return redirect('/')


def edit_book(title, author, pages, year, publisher, db_id):
    db_book = BookModel.m.find({ '_id': ObjectId(db_id) }).first()
    db_book.title = title
    db_book.author = author
    db_book.pages = pages
    db_book.year = year
    db_book.publisher = publisher
    db_book.m.save()

def list_books_as_json():
    books = BookModel.m.find().all()
    book_list = []

    for b in books:
        book_list.append(Book(b.title,
            b.author,
            b.pages,
            b.year,
            b.publisher,
            str(b._id)))

    return Enc().encode(book_list)


def add_book(title, author, pages, year, publisher):
    b = BookModel(dict(title = title,
        author = author,
        pages = pages,
        year = year,
        publisher = publisher))

    b.m.save()

def get_book(book_id):
    db_book = BookModel.m.find({ '_id': ObjectId(book_id) }).first()
    b = Book(db_book.title,
        db_book.author,
        db_book.pages,
        db_book.year,
        db_book.publisher,
        str(db_book._id))

    return b

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

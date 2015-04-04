# -*- coding: utf-8 -*-
from flask import (Flask,
        request,
        render_template,
        redirect,
        url_for)

from json import JSONEncoder

from ming import (create_datastore,
        Session,
        collection,
        Field,
        Document,
        schema)

bind = create_datastore('ggnore')
session = Session(bind)
app = Flask(__name__)

BookModel = collection(
        'reference_book', session,
        Field('_id', schema.ObjectId),
        Field('title', str),
        Field('author', str),
        Field('pages', str),
        Field('year', str),
        Field('publisher', str))

class Book:
    def __init__(self, title, author, pages, year, publisher):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        self.publisher = publisher

class Enc(JSONEncoder):
    def default(self, o):
        return o.__dict__

@app.route('/')
def main():
    return render_template('index.html',
            content = list_books_as_json())

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

        return redirect(url_for('/'))

def list_books_as_json():
    books = BookModel.m.find().all()
    book_list = []

    for b in books:
        book_list.append(Book(b.title,
            b.author,
            b.pages,
            b.year,
            b.publisher))

    return Enc().encode(book_list)

def add_book(title, author, pages, year, publisher):
    b = BookModel(dict(title = title,
        author = author,
        pages = pages,
        year = year,
        publisher = publisher))

    b.m.save()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

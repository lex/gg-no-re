# -*- coding: utf-8 -*-
from flask import (Flask,
        request,
        render_template,
        redirect,
        url_for,
        jsonify)

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

InproceedingsModel = collection('reference_inproceedings',
        session,
        Field('_id', schema.ObjectId),
        Field('author', str),
        Field('title', str),
        Field('school', str),
        Field('year', str))

ArticleModel = collection('reference_article',
        session,
        Field('_id', schema.ObjectId),
        Field('author', str),
        Field('title', str),
        Field('journal', str),
        Field('year', str),
        Field('volume', str))

class Book:
    def __init__(self, title, author, pages, year, publisher, db_id):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        self.publisher = publisher
        self.db_id = db_id
        self.bibtex = """
@Book{{<br>
    author = "{}",<br>
    title = "{}",<br>
    publisher = "{}",<br>
    year = "{}"<br>
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
@INPROCEEDINGS{{<br>
    author = "{}",<br>
    title = "{}",<br>
    school = "{}",<br>
    year = "{}"<br>
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
@ARTICLE{{<br>
    author = "{}",<br>
    title = "{}",<br>
    journal = "{}",<br>
    year = "{}",<br>
    volume = "{}"<br>
}}
""".format(author, title, journal, year, volume)

class Enc(JSONEncoder):
    def default(self, o):
        return o.__dict__

@app.route('/')
def main():
    return render_template('index.html',
            content = get_index_content(True))

@app.route('/bibtex')
def get_all_bibtex():
    all_items = get_index_content(False)
    s = ''
    print all_items
    for b in all_items['books']:
        s += (b.bibtex + '<br>')
    for a in all_items['articles']:
        s += a.bibtex + '<br>'
    for i in all_items['inproceedings']:
        s += i.bibtex + '<br>'
    return s

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

@app.route('/add_inproceedings', methods=['GET', 'POST'])
def inproceedings_adding():
    if request.method == 'GET':
        return render_template('add_inproceedings.html')
    else:
        r = request.form
        add_inproceedings(r['author'],
                r['title'],
                r['school'],
                r['year'])

        return redirect('/')

@app.route('/add_article', methods=['GET', 'POST'])
def article_adding():
    if request.method == 'GET':
        return render_template('add_article.html')
    else:
        r = request.form
        add_article(r['author'],
                r['title'],
                r['journal'],
                r['year'],
                r['volume'])

        return redirect('/')

@app.route('/delete_book/<b_id>')
def book_deleting(b_id):
    BookModel.m.remove({'_id': ObjectId(b_id)})
    return redirect('/')

@app.route('/delete_inproceedings/<i_id>')
def inproceedings_deleting(i_id):
    InproceedingsModel.m.remove({'_id': ObjectId(b_id)})
    return redirect('/')

@app.route('/delete_article/<a_id>')
def article_deleting(a_id):
    ArticleModel.m.remove({'_id': ObjectId(b_id)})
    return redirect('/')

@app.route('/edit_book/<b_id>', methods=['GET', 'POST'])
def book_editing(b_id):
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

@app.route('/edit_inproceedings/<i_id>', methods=['GET', 'POST'])
def inproceedings_editing(b_id):
    if request.method == 'GET':
        i = get_inproceedings(i_id)
        return render_template('edit_inproceedings.html', inproceedings = Enc().encode(i))
    else:
        r = request.form
        edit_inproceedings(r['author'],
                r['title'],
                r['school'],
                r['year'],
                r['db_id'])

        return redirect('/')

@app.route('/edit_article/<a_id>', methods=['GET', 'POST'])
def article_editing(a_id):
    if request.method == 'GET':
        a = get_article(a_id)
        return render_template('edit_article.html', article = Enc().encode(a))
    else:
        r = request.form
        edit_article(r['author'],
                r['title'],
                r['journal'],
                r['year'],
                r['volume'],
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

def edit_inproceedings(author, title, school, year, db_id):
    db_i = InproceedingsModel.m.find({ '_id': ObjectId(db_id) }).first()
    db_i.author = author
    db_i.title = title
    db_i.school = school
    db_i.year = year
    db_i.m.save()

def edit_article(author, title, journal, year, volume, db_id):
    db_article = ArticleModel.m.find({ '_id': ObjectId(db_id) }).first()
    db_article.author = author
    db_article.title = title
    db_article.journal = journal
    db_article.year = year
    db_article.volume = volume
    db_article.m.save()

def get_index_content(json):
    content = {}
    content['books'] = list_books()
    content['inproceedings'] = list_inproceedings()
    content['articles'] = list_articles()
    if json:
        return Enc().encode(content)
    else:
        return content

def list_books():
    books = BookModel.m.find().all()
    book_list = []

    for b in books:
        book_list.append(Book(b.title,
            b.author,
            b.pages,
            b.year,
            b.publisher,
            str(b._id)))

    return book_list

def list_inproceedings():
    inproceedings = InproceedingsModel.m.find().all()
    inproceedings_list = []

    for i in inproceedings:
        inproceedings_list.append(Inproceedings(i.author,
            i.title,
            i.school,
            i.year,
            str(i._id)))

    return inproceedings_list

def list_articles():
    articles = ArticleModel.m.find().all()
    article_list = []

    for a in articles:
        article_list.append(Article(a.author,
            a.title,
            a.journal,
            a.year,
            a.volume,
            str(a._id)))

    return article_list

def add_book(title, author, pages, year, publisher):
    b = BookModel(dict(title = title,
        author = author,
        pages = pages,
        year = year,
        publisher = publisher))

    b.m.save()

def add_inproceedings(author, title, school, year):
    i = InproceedingsModel(dict(author = author,
        title = title,
        school = school,
        year = year))

    i.m.save()

def add_article(author, title, journal, year, volume):
    a = ArticleModel(dict(author = author,
        title = title,
        journal = journal,
        year = year,
        volume = volume))

    a.m.save()

def get_book(book_id):
    db_book = BookModel.m.find({ '_id': ObjectId(book_id) }).first()
    b = Book(db_book.title,
        db_book.author,
        db_book.pages,
        db_book.year,
        db_book.publisher,
        str(db_book._id))

    return b

def get_inproceedings(inproceedings_id):
    db_i = InproceedingsModel.m.find({ '_id': ObjectId(inproceedings_id) }).first()
    i = Inproceedings(db_i.author,
        db_i.title,
        db_i.school,
        db_i.year,
        str(db_i._id))

    return i

def get_article(article_id):
    db_article = ArticleModel.m.find({ '_id': ObjectId(article_id) }).first()
    a = Article(db_article.author,
        db_article.title,
        db_article.journal,
        db_article.year,
        db_article.volume,
        str(db_article._id))

    return a

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

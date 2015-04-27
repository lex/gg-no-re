# -*- coding: utf-8 -*-
from flask import (Flask,
        request,
        render_template,
        redirect,
        url_for,
        jsonify)

import json

from ming import (create_datastore,
        Session,
        collection,
        Field,
        Document,
        schema)

from bson.objectid import ObjectId

from models import (BookModel,
        InproceedingsModel,
        ArticleModel,
        Book,
        Inproceedings,
        Article)

from database_operations import (Enc,
        delete_book,
        delete_inproceedings,
        delete_article,
        edit_book,
        edit_inproceedings,
        edit_article,
        add_book,
        add_inproceedings,
        add_article,
        get_book,
        get_inproceedings,
        get_article,
        get_index_content,
        list_books,
        list_inproceedings,
        list_articles)

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def main():
    return render_template('index.html',
            content = get_index_content(True))


@app.route('/bibtex')
def get_all_bibtex():
    all_items = get_index_content(False)
    s = ''

    for b in all_items['books']:
        s += b.bibtex + '<br>'
    for a in all_items['articles']:
        s += a.bibtex + '<br>'
    for i in all_items['inproceedings']:
        s += i.bibtex + '<br>'
    return s


@app.route('/show_single_bibtex/<db_type>/<db_id>')
def show_single_bibtex(db_type, db_id):
    if db_type == 'book':
        return get_book(db_id).bibtex
    elif db_type == 'article':
        return get_article(db_id).bibtex
    elif db_type == 'inproceedings':
        return get_inproceedings(db_id).bibtex
    else:
        return 'invalid'


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
                r['publisher'],
                r['reference'])

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
                r['year'],
                r['reference'])

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
                r['volume'],
                r['reference'])

        return redirect('/')


@app.route('/delete_book/<b_id>')
def book_deleting(b_id):
    delete_book(b_id)
    return redirect('/')


@app.route('/delete_inproceedings/<i_id>')
def inproceedings_deleting(i_id):
    delete_inproceedings(i_id)
    return redirect('/')


@app.route('/delete_article/<a_id>')
def article_deleting(a_id):
    delete_article(a_id)
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
                r['reference'],
                r['db_id'])

        return redirect('/')


@app.route('/edit_inproceedings/<i_id>', methods=['GET', 'POST'])
def inproceedings_editing(i_id):
    if request.method == 'GET':
        i = get_inproceedings(i_id)

        return render_template('edit_inproceedings.html', inproceedings = Enc().encode(i))
    else:
        r = request.form
        edit_inproceedings(r['author'],
                r['title'],
                r['school'],
                r['year'],
                r['reference'],
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
                r['reference'],
                r['db_id'])

        return redirect('/')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')


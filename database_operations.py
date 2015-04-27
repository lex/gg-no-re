# -*- coding: utf-8 -*-

from models import *
from json import JSONEncoder
from bson.objectid import ObjectId

# custom json encoder
class Enc(JSONEncoder):
    def default(self, o):
        return o.__dict__


def delete_book(db_id):
    return BookModel.m.remove({'_id': ObjectId(db_id)})


def delete_inproceedings(db_id):
    return InproceedingsModel.m.remove({'_id': ObjectId(db_id)})


def delete_article(db_id):
    return ArticleModel.m.remove({'_id': ObjectId(db_id)})


def edit_book(title, author, pages, year, publisher, reference, db_id):
    reference_free = is_reference_free(reference, db_id)
    if not reference_free:
        return False

    db_book = BookModel.m.find({ '_id': ObjectId(db_id) }).first()
    db_book.title = title
    db_book.author = author
    db_book.pages = pages
    db_book.year = year
    db_book.publisher = publisher
    db_book.reference = reference
    db_book.m.save()

    return True


def edit_inproceedings(author, title, school, year, reference, db_id):
    reference_free = is_reference_free(reference, db_id)
    if not reference_free:
        return False

    db_i = InproceedingsModel.m.find({ '_id': ObjectId(db_id) }).first()
    db_i.author = author
    db_i.title = title
    db_i.school = school
    db_i.year = year
    db_i.reference = reference
    db_i.m.save()

    return True


def edit_article(author, title, journal, year, volume, reference, db_id):
    reference_free = is_reference_free(reference, db_id)
    if not reference_free:
        return False

    db_article = ArticleModel.m.find({ '_id': ObjectId(db_id) }).first()
    db_article.author = author
    db_article.title = title
    db_article.journal = journal
    db_article.year = year
    db_article.volume = volume
    db_article.reference = reference
    db_article.m.save()

    return True


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
            b.reference,
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
            i.reference,
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
            a.reference,
            str(a._id)))

    return article_list


def add_book(title, author, pages, year, publisher, reference):
    reference_free = is_reference_free(reference)
    if not reference_free:
        return None

    b = BookModel(dict(title = title,
        author = author,
        pages = pages,
        year = year,
        publisher = publisher,
        reference = reference))

    b.m.save()
    return b._id


def add_inproceedings(author, title, school, year, reference):
    reference_free = is_reference_free(reference)
    if not reference_free:
        return None

    i = InproceedingsModel(dict(author = author,
        title = title,
        school = school,
        year = year,
        reference = reference))

    i.m.save()

    return i._id


def add_article(author, title, journal, year, volume, reference):
    reference_free = is_reference_free(reference)
    if not reference_free:
        return None

    a = ArticleModel(dict(author = author,
        title = title,
        journal = journal,
        year = year,
        volume = volume,
        reference = reference))

    a.m.save()

    return a._id


def is_reference_free(ref, db_id=None):
    b = BookModel.m.find({ 'reference': ref }).first()
    a = ArticleModel.m.find({ 'reference': ref }).first()
    i = InproceedingsModel.m.find({ 'reference': ref }).first()

    if b:
        if str(b._id) == db_id:
            return True
        return False
    if a:
        if str(a._id) == db_id:
            return True
        return False
    if i:
        if str(i._id) == db_id:
            return True
        return False

    return True


def get_book(book_id):
    db_book = BookModel.m.find({ '_id': ObjectId(book_id) }).first()
    b = Book(db_book.title,
        db_book.author,
        db_book.pages,
        db_book.year,
        db_book.publisher,
        db_book.reference,
        str(db_book._id))

    return b


def get_inproceedings(inproceedings_id):
    db_i = InproceedingsModel.m.find({ '_id': ObjectId(inproceedings_id) }).first()
    i = Inproceedings(db_i.author,
        db_i.title,
        db_i.school,
        db_i.year,
        db_i.reference,
        str(db_i._id))

    return i


def get_article(article_id):
    db_article = ArticleModel.m.find({ '_id': ObjectId(article_id) }).first()
    a = Article(db_article.author,
        db_article.title,
        db_article.journal,
        db_article.year,
        db_article.volume,
        db_article.reference,
        str(db_article._id))

    return a


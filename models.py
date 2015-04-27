# -*- coding: utf-8 -*-
from ming import (create_datastore,
        collection,
        Field,
        Document,
        schema,
        Session)

import session

BookModel = collection('reference_book',
        session.session,
        Field('_id', schema.ObjectId),
        Field('title', str),
        Field('author', str),
        Field('pages', str),
        Field('year', str),
        Field('publisher', str),
        Field('reference', str))


InproceedingsModel = collection('reference_inproceedings',
        session.session,
        Field('_id', schema.ObjectId),
        Field('author', str),
        Field('title', str),
        Field('school', str),
        Field('year', str),
        Field('reference', str))


ArticleModel = collection('reference_article',
        session.session,
        Field('_id', schema.ObjectId),
        Field('author', str),
        Field('title', str),
        Field('journal', str),
        Field('year', str),
        Field('volume', str),
        Field('reference', str))

ReferenceModel = collection('custom_reference',
        session.session,
        Field('_id', schema.ObjectId),
        Field('reference', str))


class Book:
    def __init__(self, title, author, pages, year, publisher, reference, db_id):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        self.publisher = publisher
        self.db_id = db_id
        if reference:
            self.reference = reference
        else:
            self.reference = ''
        self.bibtex = u"""
@Book{{{}<br>
    author = "{}",<br>
    title = "{}",<br>
    publisher = "{}",<br>
    year = "{}"<br>
}}
""".format(self.reference + ',', author, title, publisher, year)


class Inproceedings:
    def __init__(self, author, title, school, year, reference, db_id):
        self.author = author
        self.title = title
        self.school = school
        self.year = year
        self.db_id = db_id
        if reference:
            self.reference = reference
        else:
            self.reference = ''
        self.bibtex = u"""
@INPROCEEDINGS{{{}<br>
    author = "{}",<br>
    title = "{}",<br>
    school = "{}",<br>
    year = "{}"<br>
}}
""".format(self.reference + ',', author, title, school, year)


class Article:
    def __init__(self, author, title, journal, year, volume, reference, db_id):
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.volume = volume
        self.db_id = db_id
        if reference:
            self.reference = reference
        else:
            self.reference = ''
        self.bibtex = u"""
@ARTICLE{{{}<br>
    author = "{}",<br>
    title = "{}",<br>
    journal = "{}",<br>
    year = "{}",<br>
    volume = "{}"<br>
}}
""".format(self.reference + ',', author, title, journal, year, volume)

class Reference:
    def __init__(self, reference, db_id):
        self.reference = reference
        self.db_id = db_id

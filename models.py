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
        Field('publisher', str))


InproceedingsModel = collection('reference_inproceedings',
        session.session,
        Field('_id', schema.ObjectId),
        Field('author', str),
        Field('title', str),
        Field('school', str),
        Field('year', str))


ArticleModel = collection('reference_article',
        session.session,
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


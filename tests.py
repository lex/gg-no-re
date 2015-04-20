import unittest
from database_operations import *
from models import *
import os

book_args = ['title', 'author', 'pages', 'year', 'publisher', 'reference']
book_references = ['bookref', 'bookref2', 'bookref3']
inproceedings_args = ['author', 'title', 'school', 'year', 'reference']
ip_references = ['ipref', 'ipref2', 'ipref3']
article_args = ['author', 'title', 'journal', 'year', 'volume', 'reference']
article_references = ['articleref', 'articleref2', 'articleref3']

class TestBookOperations(unittest.TestCase):

    def test_adding(self):
        b_id = add_book(*book_args)
        self.assertTrue(b_id is not None)
        delete_book(str(b_id))

    def test_deleting(self):
        b_id = add_book(*book_args)
        result = delete_book(str(b_id))
        self.assertEqual(result, None)

    def test_getting(self):
        b_id = add_book(*book_args)
        result = get_book(str(b_id))
        self.assertEqual(result.db_id, str(b_id))
        delete_book(str(b_id))

    def test_editing(self):
        b_id = add_book(*book_args)
        old_book = get_book(str(b_id))
        edit_book('newtitle', 'newauthor', 'newpages', 'newyear', 'newpublisher', 'newbookreference', str(b_id))
        new_book = get_book(str(b_id))
        self.assertTrue(old_book.title != new_book.title)
        self.assertTrue(old_book.author != new_book.author)
        self.assertTrue(old_book.pages != new_book.pages)
        self.assertTrue(old_book.year != new_book.year)
        self.assertTrue(old_book.publisher != new_book.publisher)
        self.assertTrue(old_book.db_id == new_book.db_id)
        delete_book(str(b_id))

    def test_bibtex(self):
        b_id = add_book(*book_args)
        book = get_book(str(b_id))
        expected_bibtex = """
@Book{reference,<br>
    author = "author",<br>
    title = "title",<br>
    publisher = "publisher",<br>
    year = "year"<br>
}
"""
        self.assertEqual(book.bibtex, expected_bibtex)
        delete_book(str(b_id))

    def test_listing(self):
        b_id = add_book(*book_args)
        books = list_books()
        self.assertTrue(len(books) == 1)
        delete_book(str(b_id))

class TestInproceedingsOperations(unittest.TestCase):

    def test_adding(self):
        i_id = add_inproceedings(*inproceedings_args)
        self.assertTrue(i_id is not None)
        delete_inproceedings(str(i_id))

    def test_deleting(self):
        i_id = add_inproceedings(*inproceedings_args)
        result = delete_inproceedings(str(i_id))
        self.assertEqual(result, None)

    def test_getting(self):
        i_id = add_inproceedings(*inproceedings_args)
        result = get_inproceedings(str(i_id))
        self.assertEqual(result.db_id, str(i_id))
        delete_inproceedings(str(i_id))

    def test_editing(self):
        i_id = add_inproceedings(*inproceedings_args)
        old_ip = get_inproceedings(str(i_id))
        edit_inproceedings('newauthor', 'newtitle', 'newschool', 'newyear', 'newreference', str(i_id))
        new_ip = get_inproceedings(str(i_id))
        self.assertTrue(old_ip.author != new_ip.author)
        self.assertTrue(old_ip.title != new_ip.title)
        self.assertTrue(old_ip.school != new_ip.school)
        self.assertTrue(old_ip.year != new_ip.year)
        self.assertTrue(old_ip.db_id == new_ip.db_id)
        delete_inproceedings(str(i_id))

    def test_bibtex(self):
        i_id = add_inproceedings(*inproceedings_args)
        ip = get_inproceedings(str(i_id))
        expected_bibtex = """
@INPROCEEDINGS{reference,<br>
    author = "author",<br>
    title = "title",<br>
    school = "school",<br>
    year = "year"<br>
}
"""
        self.assertEqual(ip.bibtex, expected_bibtex)
        delete_inproceedings(str(i_id))

    def test_listing(self):
        i_id = add_inproceedings(*inproceedings_args)
        inproceedings = list_inproceedings()
        self.assertTrue(len(inproceedings) == 1)
        delete_inproceedings(str(i_id))

class TestArticleOperations(unittest.TestCase):

    def test_adding(self):
        a_id = add_article(*article_args)
        self.assertTrue(a_id is not None)
        delete_article(str(a_id))

    def test_deleting(self):
        a_id = add_article(*article_args)
        result = delete_article(str(a_id))
        self.assertEqual(result, None)

    def test_getting(self):
        a_id = add_article(*article_args)
        result = get_article(str(a_id))
        self.assertEqual(result.db_id, str(a_id))
        delete_article(str(a_id))

    def test_editing(self):
        a_id = add_article(*article_args)
        old_article = get_article(str(a_id))
        edit_article('newauthor', 'newtitle', 'newjournal', 'newyear', 'newvolume', 'newreference', str(a_id))
        new_article = get_article(str(a_id))
        self.assertTrue(old_article.author != new_article.author)
        self.assertTrue(old_article.title != new_article.title)
        self.assertTrue(old_article.journal != new_article.journal)
        self.assertTrue(old_article.year != new_article.year)
        self.assertTrue(old_article.volume != new_article.volume)
        self.assertTrue(old_article.db_id == new_article.db_id)
        delete_article(str(a_id))

    def test_bibtex(self):
        a_id = add_article(*article_args)
        article = get_article(str(a_id))
        expected_bibtex = """
@ARTICLE{reference,<br>
    author = "author",<br>
    title = "title",<br>
    journal = "journal",<br>
    year = "year",<br>
    volume = "volume"<br>
}
"""
        self.assertEqual(article.bibtex, expected_bibtex)
        delete_article(str(a_id))

    def test_listing(self):
        a_id = add_article(*article_args)
        articles = list_articles()
        self.assertTrue(len(articles) == 1)
        delete_article(str(a_id))


if __name__ == '__main__':
    if os.getenv('TEST') != 'y':
        print 'run with run_tests.sh'
    else:
        unittest.main()


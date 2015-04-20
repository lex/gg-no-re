import unittest
from database_operations import *
from models import *
import os

book_args = ['title', 'author', 'pages', 'year', 'publisher']
inproceedings_args = ['author', 'title', 'school', 'year']
article_args = ['author', 'title', 'journal', 'year', 'volume']

class TestBookOperations(unittest.TestCase):

    def test_adding(self):
        b_id = add_book(*book_args)
        self.assertTrue(b_id is not None)


    def test_deleting(self):
        b_id = add_book(*book_args)
        result = delete_book(str(b_id))
        self.assertEqual(result, None)


    def test_searching(self):
        b_id = add_book(*book_args)
        result = get_book(b_id)
        self.assertEqual(result.db_id, str(b_id))


    def test_editing(self):
        b_id = add_book(*book_args)
        old_book = get_book(str(b_id))
        edit_book('newtitle', 'newauthor', 'newpages', 'newyear', 'newpublisher', str(b_id))
        new_book = get_book(str(b_id))
        self.assertTrue(old_book.title != new_book.title)
        self.assertTrue(old_book.author != new_book.author)
        self.assertTrue(old_book.pages != new_book.pages)
        self.assertTrue(old_book.year != new_book.year)
        self.assertTrue(old_book.publisher != new_book.publisher)
        self.assertTrue(old_book.db_id == new_book.db_id)


    def test_bibtex(self):
        b_id = add_book(*book_args)
        book = get_book(str(b_id))
        expected_bibtex = """
@Book{<br>
    author = "author",<br>
    title = "title",<br>
    publisher = "publisher",<br>
    year = "year"<br>
}
"""
        self.assertEqual(book.bibtex, expected_bibtex)


    def test_listing(self):
        books = list_books()
        self.assertTrue(len(books) == 3)

class TestInproceedingsOperations(unittest.TestCase):

    def test_adding(self):
        i_id = add_inproceedings(*inproceedings_args)
        self.assertTrue(i_id is not None)


    def test_deleting(self):
         i_id = add_inproceedings(*inproceedings_args)
         result = delete_inproceedings(str(i_id))
         self.assertEqual(result, None)


    def test_searching(self):
         i_id = add_inproceedings(*inproceedings_args)
         result = get_inproceedings(str(i_id))
         self.assertEqual(result.db_id, str(i_id))


    def test_editing(self):
        i_id = add_inproceedings(*inproceedings_args)
        old_ip = get_inproceedings(str(i_id))
        edit_inproceedings('newauthor', 'newtitle', 'newschool', 'newyear', str(i_id))
        new_ip = get_inproceedings(str(i_id))
        self.assertTrue(old_ip.author != new_ip.author)
        self.assertTrue(old_ip.title != new_ip.title)
        self.assertTrue(old_ip.school != new_ip.school)
        self.assertTrue(old_ip.year != new_ip.year)
        self.assertTrue(old_ip.db_id == new_ip.db_id)


    def test_bibtex(self):
        i_id = add_inproceedings(*inproceedings_args)
        ip = get_inproceedings(str(i_id))
        expected_bibtex = """
@INPROCEEDINGS{<br>
    author = "author",<br>
    title = "title",<br>
    school = "school",<br>
    year = "year"<br>
}
"""
        self.assertEqual(ip.bibtex, expected_bibtex)


    def test_listing(self):
        inproceedings = list_inproceedings()
        self.assertTrue(len(inproceedings) == 3)

class TestArticleOperations(unittest.TestCase):

    def test_adding(self):
        a_id = add_article(*article_args)
        self.assertTrue(a_id is not None)


    def test_deleting(self):
        a_id = add_article(*article_args)
        result = delete_article(str(a_id))
        self.assertEqual(result, None)


    def test_searching(self):
        a_id = add_article(*article_args)
        result = get_article(str(a_id))
        self.assertEqual(result.db_id, str(a_id))


    def test_editing(self):
        a_id = add_article(*article_args)
        old_article = get_article(str(a_id))
        edit_article('newauthor', 'newtitle', 'newjournal', 'newyear', 'newvolume',  str(a_id))
        new_article = get_article(str(a_id))
        self.assertTrue(old_article.author != new_article.author)
        self.assertTrue(old_article.title != new_article.title)
        self.assertTrue(old_article.journal != new_article.journal)
        self.assertTrue(old_article.year != new_article.year)
        self.assertTrue(old_article.volume != new_article.volume)
        self.assertTrue(old_article.db_id == new_article.db_id)

    def test_bibtex(self):
        a_id = add_article(*article_args)
        article = get_article(str(a_id))
        expected_bibtex = """
@ARTICLE{<br>
    author = "author",<br>
    title = "title",<br>
    journal = "journal",<br>
    year = "year",<br>
    volume = "volume"<br>
}
"""
        self.assertEqual(article.bibtex, expected_bibtex)


    def test_listing(self):
        articles = list_articles()
        self.assertTrue(len(articles) == 3)


if __name__ == '__main__':
    if os.getenv('TEST') != 'y':
        print 'run with run_tests.sh'
    else:
        unittest.main()


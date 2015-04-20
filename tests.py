import unittest
from database_operations import *
from models import *
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
        self.assertTrue(old_book.title is not new_book.title)
        self.assertTrue(old_book.author is not new_book.author)
        self.assertTrue(old_book.pages is not new_book.pages)
        self.assertTrue(old_book.year is not new_book.year)
        self.assertTrue(old_book.publisher is not new_book.publisher)
        self.assertTrue(old_book.db_id == new_book.db_id)


    def test_listing(self):
        books = list_books()
        self.assertTrue(len(books) == 2)

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
        self.assertTrue(old_ip.author is not new_ip.author)
        self.assertTrue(old_ip.title is not new_ip.title)
        self.assertTrue(old_ip.school is not new_ip.school)
        self.assertTrue(old_ip.year is not new_ip.year)
        self.assertTrue(old_ip.db_id == new_ip.db_id)


    def test_listing(self):
        inproceedings = list_inproceedings()
        self.assertTrue(len(inproceedings) == 2)

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
        self.assertTrue(old_article.author is not new_article.author)
        self.assertTrue(old_article.title is not new_article.title)
        self.assertTrue(old_article.journal is not new_article.journal)
        self.assertTrue(old_article.year is not new_article.year)
        self.assertTrue(old_article.volume is not new_article.volume)
        self.assertTrue(old_article.db_id == new_article.db_id)


    def test_listing(self):
        articles = list_articles()
        self.assertTrue(len(articles) == 2)


if __name__ == '__main__':
    unittest.main()


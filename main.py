# -*- coding: utf-8 -*-

from flask import Flask, flash, request, render_template
from json import JSONEncoder
app = Flask(__name__)

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

class Enc(JSONEncoder):
    def default(self, o):
        return o.__dict__

@app.route('/')
def main():
    return 'sick welcome screen with zooming stuff'

@app.route('/<page_number>')
def paged(page_number):
    return give_page(page_number)

def give_page(number):
    b = Book('Juuh vol. 5', 'Juuh Elikkäs')
    return render_template('list.html', json = Enc().encode(b));

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

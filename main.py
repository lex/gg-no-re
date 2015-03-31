from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return 'sick welcome screen'

@app.route('/list/<page_number>')
def paged(page_number):
    return give_page(page_number)

def give_page(number):
    return number;

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

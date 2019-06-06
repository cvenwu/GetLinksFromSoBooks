from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from tool.crawl_tool import *
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/itbook')
def itbook():
    root_url = "https://sobooks.cc"
    for url in get_category_link(root_url):
        analy_url_page(url)
    return render_template('it_book.html')


@app.route('/sobook')
def sobook():

    return render_template('sobook.html')

if __name__ == '__main__':
    app.run(debug=True)
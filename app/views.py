from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''View root page fn that returns the index page and its data'''
    title = 'News-API'
    return render_template('index.html', title=title)




@app.route('/about/<source_id>')
def about(source_id):

    # articles = get_articles(source_id)
    return render_template('news.html', id = source_id)


 
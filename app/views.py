from flask import render_template
from app import app
from .request import get_sources,get_source,search_source

#Views
@app.route('/')
def index():
    '''View root page fn that returns the index page and its data'''
    #Getting  business sources
    business_sources=get_sources('business')
    technology_sources=get_sources('technology')
    general_sources=get_sources('general')
    title = 'News-API'
    return render_template('index.html', title=title,business=business_sources,technology=technology_sources,general=general_sources)

@app.route('/source/<id>')
def source(id):

    source= get_source('id')
    name = f'{source.name}'


    return render_template('news.html',name=name,source=source)
# @app.route('/')

# @app.route('/about/<source_id>')
# def about(source_id):

#     # articles = get_articles(source_id)
#     return render_template('news.html', id = source_id)


 
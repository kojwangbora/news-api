from flask import render_template,request,redirect,url_for
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

    search_source= request.args.get('search_query')

    if search_source:
        return redirect(url_for('search',source_name=search_source))
    else:
        return render_template('index.html', title=title,business=business_sources,technology=technology_sources,general=general_sources)

@app.route('/news/<id>')
def news(id):

    source= get_source('id')
    name = f'{source.name}'


    return render_template('news.html',name=name,source=source)

@app.route('/search/<source_name>')
def search(source_name):
    '''View fn that displas the search results'''
    source_name_list =source_name.split("")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    id = f'search results for {source_name}'
    return render_template('search.html',sources = searched_sources)
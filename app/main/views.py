from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles

#Views
@main.route('/')
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

@main.route('/news/<source_id>')
def news(source_id):

    # source= source('id')
    # name = f'{source.name}'
    articles= get_articles('business')


    return render_template('news.html',article=articles)

 
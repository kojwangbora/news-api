from app import app
import urllib.request,json
from .models import source
# import request

Source=source.Source

#Getting api key

api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["MOVIE_API_BASE_URL"]

def get_sources(category):
    '''function gets json resonse to the url request'''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        response =json.loads(get_sources_data)

        source_results= None

        if response['sources']:
            sources_results_list = response['source']
            sources_results = process_new_sources(sources_results_list)

    return sources_results
def process_new_sources(sources_list):
    sources_results =[]

    for sources_item in sources_list:
        urlToImage= sources_item.get('urlToImage')
        url=sources_item.get('url')
        title=sources_item.get('title')
        content=sources_item.get('content')
        author=sources_item.get('author')
        publishedAt=sources_item('publishedAt')
        
    return sources_results
            

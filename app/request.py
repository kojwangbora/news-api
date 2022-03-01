from app import app
import urllib.request,json
from .models import articles, news_source
# import request

Source=news_source.Source

#Getting api key

apiKey = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(category):
    '''function gets json resonse to the url request'''
    get_sources_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        response =json.loads(get_sources_data)

        source_results= None

        if response['sources']:
            sources_results_list = response['sources']
            sources_results = process_new_sources(sources_results_list)

    return sources_results
    
def process_new_sources(sources_list):
    sources_results =[]

    for sources_item in sources_list:
        id= sources_item.get('id')
        name = sources_item.get('name')
        url=sources_item.get('url')
        description=sources_item.get('description')
        category=sources_item.get('category')
        language=sources_item.get('language')
        country=sources_item.get('country')

        source_object= Source(id,name,url,description,category,language,country)
        sources_results.append(source_object)
        
    return sources_results

def get_source(id):
    get_source_details_url = base_url.format(id,apiKey)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        source_object = None
        if source_details_response:
            id=source_details_response.get('id')
            name = source_details_response.get('name')
            url=source_details_response.get('url')
            description=source_details_response.get('description')
            category=source_details_response.get('category')
            language=source_details_response.get('language')
            country=source_details_response.get('country')

            source_object=Source(id,name,url,description,category,language,country)
    
    return source_object

def search_source(source_name):
    search_source_url='https://newsapi.org/v2/sources?category={}&apiKey={}'.format(apiKey,source_name)
    with urllib.request.urlopen(search_source_url) as url:
        search_source_data = url.read()
        search_source_response= json.loads(search_source_data)

        search_source__results=None

        if search_source_response['results']:
            search_source_list=search_source_response['results']
            search_source__results =process_new_sources(search_source_list)



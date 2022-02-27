from app import app
import urllib.request,json
from .models import source
# import request

Source=source.Source

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
            

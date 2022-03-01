from app import app
import urllib.request,json
from .models import articles,source
# import request

Source=source.Source
Article=articles.Articles

#Getting api key

apiKey = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

#getting the articles base url
article_url= app.config["ARTICLE_API_BASE_URL"]

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

def get_articles(source_id):
    '''function gets json resonse to the url request'''
    get_articles_url = article_url.format(source_id,apiKey)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        response =json.loads(get_articles_data)

        articles_results= None

        if response['articles']:
            articles_results_list = response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_articles(article_list):
     
    articles_results =[]
    for articles_details_response in article_list:
        urlToImage=articles_details_response.get('urlToImage')
        url = articles_details_response.get('url')
        title=articles_details_response.get('title')
        content=articles_details_response.get('content')
        author=articles_details_response.get('author')
        publishedAt=articles_details_response.get('publishedAt')


            
            

        articles_object=Article(urlToImage,url,title,content,author,publishedAt)
            
        articles_results.append(articles_object)

    return articles_results

 



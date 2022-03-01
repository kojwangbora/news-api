import os
class Config:
    '''General configuration parent class'''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}' 
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'  
    NEWS_API_KEY = os.environ.get('SECRET_')




class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}

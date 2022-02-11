class Config:
    '''
    parent class for all config and sub classes
    '''
    ALL_ARTICLES_BASE_URL="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}"
    TECH_CRUNCH_BASE_URL = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={}"
    BUSINESS_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={}'
    TESLA_BASE_URL = "https://newsapi.org/v2/everything?q=tesla&from=2021-12-29&sortBy=publishedAt&apiKey={}"
    APPLE_BASE_URL = 'https://newsapi.org/v2/everything?q=apple&from=2022-01-28&to=2022-01-28&sortBy=popularity&apiKey={}'

class ProdConfig(Config):
    '''
    child of the Config class
    '''
    pass
class DevConfig(Config):
    '''
    child of the Config class
    '''
    DEBUG = True
    
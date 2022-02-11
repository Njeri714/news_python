from app import app
import request
from .config import Config
import os
from .models import news

News_article = news.News

Api_key = os.getenv('NEWS_API_KEY')
tech_base_url = app.config['TECH_CRUNCH_BASE_URL']
business_base_url=app.config['BUSINESS_BASE_URL']
all_article_base_url= app.config['ALL_ARTICLES_BASE_URL']
apple_base_url = app.config['APPLE_BASE_URL']
tesla_base_url= app.config['TESLA_BASE_URL'] 

def tech_news():
    base_url = tech_base_url.format(Api_key)
    tech_data = request.get(base_url).json()
    tech_news = []

    for tech in tech_data['articles']:
        id = tech['source']
        title = tech['title']
        poster = tech['urlToImage']
        url_link = tech['url']
        description = tech['description']
        published_date = tech['publishedAt']
        content = tech['content']
        
        tech_object = News_article(id, title, poster, url_link, description, published_date, content)
        tech_news.append(tech_object)
    return tech_news


def all_articles_news():
    '''
    all_articles_news function displays all news from various sources without specification
    '''
    base_url = all_article_base_url.format(Api_key)
    all_article_data = requests.get(base_url).json()
    all_articles = []
    data_articls = all_article_data.get('articles')
    print(type(data_articls),all_article_data)
    for articles_data in all_article_data['articles'] :
        id = articles_data.get('source')
        title = articles_data.get('title')
        poster = articles_data.get('urlToImage')
        url_link = articles_data.get('url')
        description = articles_data.get('description')
        published_date = articles_data.get('publishedAt')
        content = articles_data.get('content')
        
        articles_object = News_article(id, title, poster, url_link, description, published_date, content)
        all_articles.append(articles_object)

    return all_articles

def business_news():
    '''
    business_news function for getting data about us business operations
    '''
    base_url = business_base_url.format(Api_key)
    bussiness_articles = requests.get(base_url).json()
    business_data = []
    for business in bussiness_articles ['articles']:
        id = business['source']
        title = business['title']
        poster = business['urlToImage']
        url_link = business['url']
        description = business['description']
        published_date = business['publishedAt']
        content = business['content']
        
        articles_object = News_article(id, title, poster, url_link, description, published_date, content)
        business_data .append(articles_object)

    return business_data

def apple_news():
    '''
    apple_news function will handle getting of data from the api, data about apple news
    '''
    base_url = apple_base_url.format(Api_key)
    apple_articles = requests.get(base_url).json()
    apple_data = []
    for apple in apple_articles['articles']:
        id = apple['source']
        title = apple['title']
        poster = apple['urlToImage']
        url_link = apple['url']
        description = apple['description']
        published_date = apple['publishedAt']
        content = apple['content']
        
        articles_object = News_article(id, title, poster, url_link, description, published_date, content)
        apple_data .append(articles_object)
           
    return apple_data

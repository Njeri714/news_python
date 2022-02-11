from urllib.request import Request
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
    all_article_data = Request.get(base_url).json()
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


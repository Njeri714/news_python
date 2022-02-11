from app import app
import requests
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

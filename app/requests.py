from app import app
import urllib.request,json
from .models import source, articles

Source = source.Source
Articles = articles.Articles

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']


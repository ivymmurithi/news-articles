from app import app
import urllib.request,json

from app.source_tests import NewsTest
from .models import source, articles

Source = source.Source
Articles = articles.Articles

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):

    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    news_results = []

    for news_item in news_list:
        name = news_item.get('name')
        url = news_item.get('url')
        title = news_item.get('title')
        author = news_item.get('author')
        description = news_item.get('description')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
        urlToImage = news_item.get('urlToImage')


        source_object = Source(name,url)
        articles_object = Articles(name,title,url,author,description,publishedAt,content,urlToImage)
        news_results.append(source_object,articles_object)

    return news_results
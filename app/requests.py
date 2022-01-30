from app import app
import urllib.request,json
from .models import source, articles

Source = source.Source
Articles = articles.Articles

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']

def get_news(source):

    get_news_url = base_url.format(source,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

        return news_results

def process_results(news_list):
    news_results = []

    for news_item in news_list:
        name = news_item.get('source.name')
        url = news_item.get('source.url')
        description = news_item.get('source.description')


        source_object = Source(name,url,description)
        news_results.append(source_object)

    return news_results

def news_articles(articles):
    get_articles_url = base_url.format(articles,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_news_response = json.loads(get_articles_data)

        articles_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            articles_results = process_results(news_results_list)


    return articles_results

def process_results(articles_list):

    articles_results = []
    for article in articles_list:
        name = article.get('name')
        url = article.get('url')
        title = article.get('title')
        author = article.get('author')
        description = article.get('description')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        urlToImage = article.get('urlToImage')

        articles_object = Articles(name,title,url,author,description,publishedAt,content,urlToImage)
        articles_results.append(articles_object)

    return articles_results
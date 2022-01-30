from flask import render_template
from app import app
from app.models import articles
from .requests import get_news,news_articles
# from .models import source,articles

@app.route('/')
def source():
    display_sources = get_news('sources')

    return render_template('source.html', sources = display_sources)

# @app.route('/news/<news_name>')
# def news(news_name):

#     return render_template('articles.html',name =  news_name)

@app.route('/articles')
def articles():
    display_articles = news_articles('articles')
    return render_template('articles.html', articles =  display_articles)
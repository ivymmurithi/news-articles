from flask import render_template
from app import app
from .requests import get_news,news_articles
# from .models import source,articles

@app.route('/')
def source():
    display_sources = get_news('sources')
    title = 'Home - News Sources WorldWide'
    return render_template ('source.html', title = title, sources = display_sources)

@app.route('/news/<news_name>')
def news(news_name):

    return render_template('articles.html',name =  news_name)
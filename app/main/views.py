from flask import render_template
from . import main
from ..requests import get_news,news_articles


@main.route('/')
def source():
    display_sources = get_news('sources')
    print(display_sources)
    return render_template('source.html', sources = display_sources)

@main.route('/articles')
def articles():
    display_articles = news_articles('articles')
    return render_template('articles.html', articles =  display_articles)
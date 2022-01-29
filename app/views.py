from flask import render_template
from app import app

@app.route('/')
def source():

    message = 'Hello WOrld'
    return render_template('source.html', message = message)

@app.route('/news/<news_name>')
def news(news_name):

    return render_template('articles.html',name =  news_name)
from flask import render_template
from app import app

@app.errorhandler(404)
def notfound(error):
    return render_template('error.html'),404
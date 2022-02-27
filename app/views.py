from email import message
from email.mime import text
from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''View root page fn that returns the index page and its data'''

    text = 'Hello World!'
    return render_template('index.html', text= text)

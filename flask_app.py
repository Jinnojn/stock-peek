
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Puttipat web'

@app.route('/stock-peek')
def stock_peek():
    return 'Puttipat web'

@app.route('/today')
def day():
    return str(date.today())

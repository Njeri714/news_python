from flask import render_template
from app import app

from .request import requests


@app.route('/')
def homepage():
    base_url = "https://newsapi.org/v2/everything?q=Apple&from=2022-01-26&sortBy=popularity&apiKey=ffb788ce77dc47d3aa4d36f8cccc8f43"
    data = requests.get(base_url).json()
    return render_template("index.html", data=[data])

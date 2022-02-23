# -*- coding: utf-8 -*-
# Flaskパッケージをインポート
from flask import Flask, request, Response
import requests
# from bs4 import BeautifulSoup

# Flaskクラスのインスタンス生成
app = Flask(__name__)

# URLを指定。URLにリクエストが来ると関数が実行される
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    """
    html = res.text
    sorp = BeautifulSoup(html, 'html.parser')
    title = sorp.find('title')
    return title.text
    """
    print(path)
    res = requests.get('https://api.github.com/users/taiga-tech')
    return res.json()

@app.route('/search')
def analyzer():
    query = ""
    if request.args.get('q') is not None:
        query = request.args.get('q')
    else:
        query = "パラメーターがないよ"
    return query

@app.route('/favicon.ico')
def favicon():
    return ""

if __name__ == '__main__':
	app.run(debug=True)

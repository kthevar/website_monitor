import os
from flask import Flask, render_template, jsonify
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/')
def index():
    results = get_http_status()
    return render_template('index.html', results=results)

def get_http_status():
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']

    with open('urls.txt', 'r') as file:
        urls = file.read().strip().splitlines()

    results = []

    for url in urls:
        try:
            response = requests.get(url, auth=HTTPBasicAuth(username, password))
            results.append({'url': url, 'status_code': response.status_code})
        except requests.exceptions.RequestException as e:
            results.append({'url': url, 'error': str(e)})

    return results

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

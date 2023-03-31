import os
import time
from flask import Flask, render_template, jsonify
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_status')
def check_status():
    results = get_http_status()
    return jsonify(results)

def get_http_status():
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']

    with open('urls.txt', 'r') as file:
        urls = file.read().strip().splitlines()

    results = []

    for url in urls:
        try:
            start_time = time.time()
            response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=30)
            response_time = round((time.time() - start_time) * 1000, 2)  # in milliseconds
            results.append({'url': url, 'status_code': response.status_code, 'response_time': response_time})
        except requests.exceptions.RequestException as e:
            results.append({'url': url, 'error': str(e)})

    return results

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

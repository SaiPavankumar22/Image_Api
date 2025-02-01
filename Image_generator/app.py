# app.py
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

ACCESS_KEY = "your-api-key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('keyword')
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "client_id": ACCESS_KEY,
        "per_page": 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            image_url = data["results"][0]["urls"]["regular"]
            image_link = data["results"][0]["links"]["html"]
            return jsonify({"image_url": image_url, "image_link": image_link})
        else:
            return jsonify({"error": "No images found."})
    else:
        return jsonify({"error": "Error fetching data from Unsplash."})

if __name__ == '__main__':
    app.run(debug=True)

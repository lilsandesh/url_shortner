# app.py
from flask import Flask, request, redirect, render_template, jsonify
from url_shortener import URLShortener

app = Flask(__name__)
url_shortener = URLShortener()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form.get('url')
        custom_alias = request.form.get('alias')
        try:
            short_url = url_shortener.shorten_url(original_url, custom_alias)
            return render_template('index.html', short_url=short_url)
        except ValueError as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html')

@app.route('/<short_key>')
def redirect_to_original(short_key):
    original_url = url_shortener.get_original_url(short_key)
    if original_url:
        return redirect(original_url)
    return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=6000)


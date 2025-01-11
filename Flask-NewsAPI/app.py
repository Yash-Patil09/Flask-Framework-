from flask import Flask,render_template,request,url_for
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='e3f509754a9f4786bfdd6f1d628e6157')

@app.route('/')
def home():
    return render_template('index.html')

# Fetch news route
@app.route('/news', methods=['POST'])
def get_news():
    query = request.form.get('query')  # User input for topic
    if not query:
        query = "latest"  # Default query if no input is provided

    # Fetching news using NewsAPI
    try:
        top_headlines = newsapi.get_everything(
            q=query,
            language='en',
            sort_by='relevancy',
            page_size=8
        )

        articles = top_headlines.get('articles', [])
        return render_template('index.html', articles=articles, query=query)
    except Exception as e:
        error_message = str(e)
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
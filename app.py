from flask import Flask, jsonify
from scraper import scrape_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/user/<string:username>')
def index(username):
    response_data = scrape_data(username)
    if response_data == None:
        return jsonify({
            'response': {
                'error': "Can't find data."
            }
        }), 404
        
    return jsonify({
        'response': response_data
    }), 200

if __name__ == '__main__':
    app.run(debug=True)

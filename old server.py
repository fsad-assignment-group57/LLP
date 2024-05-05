# Sampada's Python Backend

from flask import Flask, jsonify, request

app = Flask(__name__)

registered_languages = {}  # Dictionary to store registered languages for users

@app.route('/api/register_languages', methods=['POST'])
def register_languages():
    # Implement logic to store registered languages for a user
    data = request.get_json()
    user_id = data['user_id']
    languages = data['languages']
    registered_languages[user_id] = languages
    return jsonify({'message': 'Registered languages for user successfully.'})

@app.route('/api/fetch_languages/<user_id>')
def fetch_languages(user_id):
    # Implement logic to fetch registered languages for a user
    if user_id in registered_languages:
        return jsonify({'user_id': user_id, 'languages': registered_languages[user_id]})
    else:
        return jsonify({'message': 'User not found.'}), 404

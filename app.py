from flask import Flask, request, jsonify, send_from_directory
from chatbot import get_answer

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get('message', ''))[:500]
    return jsonify(answer=get_answer(message))

if __name__ == '__main__':
    app.run(debug=True)
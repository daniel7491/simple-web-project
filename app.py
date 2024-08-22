from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

# Serve static files (HTML, CSS, JS)
@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

# API endpoint
@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Hello from the server!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

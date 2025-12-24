from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello from CI/CD Pipeline!", status="success")

@app.route('/health')
def health():
    return jsonify(status="healthy"), 200

def add_numbers(a, b):
    """Fonction simple pour tester"""
    return a + b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
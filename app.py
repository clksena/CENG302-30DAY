from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Merhaba! Bu benim basit backend projem.")

@app.route('/api/data')
def data():
    example_data = {
        "id": 1,
        "name": "Sena'nın Web Sitesi",
        "description": "Bu veri backend tarafından sağlanıyor."
    }
    return jsonify(example_data)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Basit Form</h1>
        <form action="/submit" method="post">
            <input type="text" name="kullanici_adi" placeholder="Kullanıcı Adı">
            <input type="submit" value="Gönder">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    kullanici_adi = request.form.get('kullanici_adi')
    if kullanici_adi:
        return jsonify(message=f"Merhaba {kullanici_adi}! Form başarıyla gönderildi.")
    else:
        return jsonify(error="Kullanıcı adı eksik."), 400

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request

server = Flask(__name__)

@server.route('/vectorizer', methods=['POST'])
def vectorizer():
    data = request.get_json()
    print(data)
    return {'vector': [1, 2, 3]}

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=8080)
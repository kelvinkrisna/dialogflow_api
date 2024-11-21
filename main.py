from flask import Flask
from random_address import real_random_address

app = Flask(__name__)

@app.route('/', methods=['GET'])
def studentNumber():
    return {'studentnumber': '200585799'}

@app.route('/webhook', methods=['GET', 'POST'])
def bagposition():
    customaddress = real_random_address()
    return customaddress

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
from flask import Flask
from random_address import real_random_address

app = Flask(__name__)

@app.route('/', methods=['GET'])
def studentNumber():
    return {'studentnumber': '200585799'}

@app.route('/webhook', methods=['GET'])
def bagposition():
    customaddress = real_random_address(
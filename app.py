import json
from flask import Flask

app = Flask(__name__)

payload = {
    'name': 'Status Quo'
}
index_payload = {
    'name': 'I am Charlie Meadows'
}


@app.route('/rockband')
def rock_band():
    return json.dumps(payload)


@app.route('/')
def index():
    return json.dumps(index_payload)


if __name__ == '__main__':
    pass

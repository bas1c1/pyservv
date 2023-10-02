from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

import os
from flask import send_from_directory

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

@app.route('/<path:path>', methods=['GET'])
def serve_file_in_dir(path):

    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = os.path.join(path, 'GTA_SA.zip')

    return send_from_directory(static_file_dir, path)

app.run(host='0.0.0.0',port=8080)


if __name__ == '__main__':
    app.run()

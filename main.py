from flask import Flask
from flask import send_from_directory
import os

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def hello():
    return send_from_directory(app.static_folder, "GTA_SA.zip")

if __name__ == '__main__':
    app.run(threaded=True, port=8080)

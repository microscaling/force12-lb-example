from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
hostname = os.environ.get('HOSTNAME')

@app.route('/')
def hello_world():
    return render_template("hello.html", hostname=hostname)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
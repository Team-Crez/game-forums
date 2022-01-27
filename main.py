import sys
from scripts import *
from flask import Flask, render_template

from scripts.args import ArgumentParser
from scripts.file import FlaskFileReader

flask_properties = {
    "template_folder": "web"
}

app = Flask(__name__, **flask_properties)
flaskReader = FlaskFileReader(template_folder=flask_properties["template_folder"])

@app.route('/')
def hello():
    return render_template("index.html", banner="src/banner.png")

@app.route('/src/<file>')
def load_source(file):
    return flaskReader.readWeb('src/' + file)

if __name__ == '__main__':
    args = ArgumentParser.parse_args(sys.argv)
    if '-debug' in args:
        app.run(debug=True, host='127.0.0.1')
    else:
        app.run()
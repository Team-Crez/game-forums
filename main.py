import sys, copy
from scripts import *
from flask import Flask, Response, abort, render_template

from scripts.args import ArgumentParser
from scripts.file import FlaskFileReader
from scripts.image import ImageModifier
from scripts.mime import MIMEType

flask_properties = {
    "template_folder": "web"
}

global_scripts = [
    "string.js",
    "image_loader.js",
    "element_scaler.js",
    "https_redirection.js"
]

def get_global_scripts():
    result = copy.copy(global_scripts)
    if app.debug:
        if "https_redirection.js" in result:
            result.remove("https_redirection.js")
    return result

app = Flask(__name__, **flask_properties)
flaskReader = FlaskFileReader(template_folder=flask_properties["template_folder"])

@app.route('/')
def hello():
    main_prop = {
        "banner": "src/banner",
        "global_scripts": get_global_scripts()
    }

    return render_template("index.html", **main_prop)

@app.route('/src/<path:file>')
def load_source(file):
    try:
        return Response(flaskReader.readWeb('src/' + file), mimetype=MIMEType.get_mimetype(file))
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    args = ArgumentParser.parse_args(sys.argv)
    flask_args = {
        'host': '0.0.0.0'
    }

    if '-debug' in args: flask_args['debug'] = True
    if '-local' in args: flask_args['host'] = '127.0.0.1'

    resized_images = ImageModifier.image_resizer(["./web/src/banner.png"], [0.8, 0.6, 0.4, 0.2])[1]
    ImageModifier.image_changer(resized_images, 'webp', lossless=False)
    app.run(**flask_args)


import sys, copy

import flask
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
    if flask_args['debug']:
        if "https_redirection.js" in result:
            result.remove("https_redirection.js")
    return result

app = Flask(__name__, **flask_properties)
flaskReader = FlaskFileReader(template_folder=flask_properties["template_folder"])

default_prop = {
    "embed_metadata": [
        ["통합 비공식 포럼", "og:title"],
        ["Team Crez에서 개발 중인 얼불춤 & 리듬닥터 통합 비공식 포럼입니다", "og:description"],
        ["https://game-forums.herokuapp.com", "og:url"],
        ["https://game-forums.herokuapp.com/src/banner_x0.2.webp", "og:image"],
        ["#fc7b03", "theme-color"] # rgb(252, 123, 3) -> #fc7b03
    ]
}

def get_prop(prop):
    result = copy.copy(default_prop)
    for key, value in prop.items():
        result[key] = value
    
    return result

@app.route('/')
def hello():
    main_prop = {
        "banner": "src/banner"
    }

    return render_template("index.html", **get_prop(main_prop))

@app.route('/src/<path:file>')
def load_source(file):
    try:
        return Response(flaskReader.readWeb('src/' + file), mimetype=MIMEType.get_mimetype(file))
    except FileNotFoundError:
        abort(404)

def start():
    global flask_args, resized_images, default_prop
    args = ArgumentParser.parse_args(sys.argv)
    flask_args = {
        'host': '0.0.0.0'
    }

    if '-debug' in args: flask_args['debug'] = True
    else: flask_args['debug'] = False

    if '-local' in args: flask_args['host'] = '127.0.0.1'

    default_prop["global_scripts"] = get_global_scripts()

    resized_images = ImageModifier.image_resizer(["./web/src/banner.png"], [0.8, 0.6, 0.4, 0.2])[1]
    ImageModifier.image_changer(resized_images, 'webp', lossless=False)

    app.run(**flask_args)

start()


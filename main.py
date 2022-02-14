import io, socket
import time, signal
import os, sys, copy
from tokenize import String

import requests
from flask import Flask, Response, abort, render_template, request
from _thread import start_new_thread

from scripts.args import ArgumentParser
from scripts.file import FlaskFileReader
from scripts.image import ImageModifier
from scripts.mime import MIMEType
from scripts.websys import WebReader

# 스크립트 설정
script_prop = {
    "gtag_id": "TM36CC4"
}

# Flask 설정
flask_properties = {
    "template_folder": "web"
}

# 모든 웹 페이지에 적용되는 스타일 설정
global_styles = [
    "global.css"
]

# 모든 웹 페이지에 적용되는 스크립트 설정
global_scripts = [
    # 필수 스크립트
    "src/js/offline.js",

    # 외부 모듈
    "https://github.com/js-cookie/js-cookie/releases/download/v3.0.1/js.cookie.min.js",
    "src/js/sha512.min.js",
    
    # 내부 모듈
    "src/js/https_redirection.js",
    "src/js/image_loader.js",
    "src/js/string.js",

    # 사이트 구성요소
    "src/js/element_scaler.js",
    "src/js/level_loader.js",
]

def get_global_scripts():
    result = copy.copy(global_scripts)
    if flask_args['debug']:
        if "src/js/https_redirection.js" in result:
            result.remove("src/js/https_redirection.js")
    return result

def timeout(sec):
    time.sleep(sec)
    os.kill(os.getpid(), signal.SIGTERM)

app = Flask(__name__, **flask_properties)
flaskReader = FlaskFileReader(template_folder=flask_properties["template_folder"])
local_addr = socket.gethostbyname(socket.gethostname())
domain = "game-forums.herokuapp.com"

# 모든 웹 페이지에 적용되는 설정
default_prop = {
    "title": "Game Forums",
    "gtag_script": "src/js/gtag_manager.js",
    "metadata": [
        # 소유권 확인
        ["-5mrPsvvBLfpLAMYBsbmLYzsVI6mLpjrs8xvNpaESDI", "google-site-verification"],

        # 뷰포트와 사이트 설정
        ["width=device-width, initial-scale=1.0", "viewport"],
        ["Team Crez에서 개발 중인 얼불춤 & 리듬닥터 통합 비공식 포럼입니다", "description"],

        # Embed 데이터
        ["통합 비공식 포럼", "og:title"],
        ["Team Crez에서 개발 중인 얼불춤 & 리듬닥터 통합 비공식 포럼입니다", "og:description"],
        ["https://game-forums.herokuapp.com", "og:url"],
        ["https://game-forums.herokuapp.com/src/banner.webp?scale=0.2", "og:image"],
        ["#fc7b03", "theme-color"] # rgb(252, 123, 3) -> #fc7b03
    ]
}

def get_prop(prop):
    result = copy.copy(default_prop)
    for key, value in prop.items():
        result[key] = value
    
    return result

@app.route('/')
def main():
    main_prop = {
        "banner": "src/banner"
    }

    return render_template("index.html", **get_prop(main_prop))

@app.route('/<file>')
def pages(file):
    main_prop = {
        "banner": "src/banner"
    }
    
    if os.path.isfile("web/" + file):
        if MIMEType.get_mimetype("web/" + file) == "text/html":
            return render_template(file, **get_prop(main_prop))
        else:
            return Response(flaskReader.readMinWeb(file, **script_prop), mimetype=MIMEType.get_mimetype("web/" + file))
    else: abort(404)

@app.route('/src/<path:file>')
def load_source(file):
    try:
        if MIMEType.is_image(file):
            img = flaskReader.loadImg("src/" + file)
            if request.args.get("scale", 0):
                byteIO = io.BytesIO()
                try:
                    size = float(request.args.get("scale"))
                except ValueError:
                    abort(400)

                try:
                    img = ImageModifier.resize_image(img, size)
                except ValueError:
                    abort(406)
                
                img.save(byteIO, MIMEType.get_mimetype('' + file).replace("image/", ""))
                byteIO.seek(0)

                return Response(byteIO, mimetype=MIMEType.get_mimetype(file))
        return Response(flaskReader.readMinWeb('src/' + file, **script_prop), mimetype=MIMEType.get_mimetype(file))
    except FileNotFoundError:
        abort(404)

def start():
    global flask_args, resized_images, default_prop, global_scripts
    args = ArgumentParser.parse_args(sys.argv)
    flask_args = {
        'host': '0.0.0.0',
        'port': 80
    }

    if '-debug' in args:
        flask_args['host'] = local_addr
        script_prop["gtag_id"] = ""
        flask_args['debug'] = True
        flask_args['port'] = 5000
    else:
        flask_args['debug'] = False

    if '-local' in args: flask_args['host'] = '127.0.0.1'

    req_addr = flask_args['host']
    if 'HEROKU_ENV' in os.environ: req_addr = domain
    
    default_prop["global_scripts"] = get_global_scripts()
    default_prop["global_styles"] = global_styles

    default_prop["gtag_id"] = script_prop["gtag_id"]

    def requester(path):
        return requests.get("http://{}:{}/{}".format(req_addr, flask_args['port'], path))

    default_prop["web_reader"] = WebReader(requester)

    if '-timeout' in args:
        start_new_thread(timeout, (float(args['-timeout']), ))

    if not 'HEROKU_ENV' in os.environ: app.run(**flask_args)

start()


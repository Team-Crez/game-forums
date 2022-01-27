import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>통합포럼에 오신 것을 환영합니다!</h1>'

if __name__ == '__main__':
    # app.run(debug=True, host='127.0.0.1')
    app.run()
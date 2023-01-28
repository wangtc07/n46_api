# save this as app.py
import flask
from route.routing import param

app = flask.Flask(__name__)
app.register_blueprint(param)

# JSON_AS_ASCII 初期值為 True, 中日文會亂碼
app.config['JSON_AS_ASCII'] = False


@app.after_request
def after_request(res):
    res.headers.add('Access-Control-Allow-Origin', '*')
    res.headers.add('Access-Control-Allow-Headers', 'Content-Type')  # ORIGIN 跨域
    res.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

    return res


@app.route("/")
@app.route("/hello")
def hello():
    return "Hello, World!"


if __name__ == '__main__':
    app.run()

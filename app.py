# save this as app.py
import flask
from routing import param
app = flask.Flask(__name__)
app.register_blueprint(param)

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
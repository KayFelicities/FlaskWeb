"""main page"""
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.redirect("http://127.0.0.1:8023")

if __name__ == '__main__':
    app.run()
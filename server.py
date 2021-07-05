from ap import *
from flask import jsonify, Flask, request
app = Flask(__name__)


@app.route("/america")
def america():
    metarmap().america()
    return "<p>success<P>"


@app.route("/metars")
def metar():
    metarmap().metars()
    return "<p>success<P>"


@app.route("/test")
def test():
    metarmap().test()
    return "<p>success<P>"


def run():
    app.run(host="0.0.0.0", port=3333)


run()

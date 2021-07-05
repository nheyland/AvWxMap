from ap import *
from flask import jsonify, Flask, request
app = Flask(__name__)


@app.route("/america")
def america():
    metarmap().america()
    return "<p>success<P>"


@app.route("/metar")
def metar():
    metarmap().metar()
    return "<p>success<P>"


@app.route("/test")
def test():
    metarmap().test()
    return "<p>success<P>"


def run():
    print(request.remote_addr)
    app.run(host="0.0.0.0", port=3333)


run()

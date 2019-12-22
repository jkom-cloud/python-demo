import time
import datetime

from flask import Flask
from flask import jsonify

from lib import fib

app = Flask(__name__)


@app.route('/')
def index():
    """Welcome page"""
    now = datetime.datetime.now().isoformat()
    return jsonify(message='Hello World!!', ts=now)


@app.route('/ping/')
def ping():
    """ping"""
    return 'pong'


@app.route('/fib/seq/<int:n>/')
def fib_seq(n):
    """Get Fibonacci sequence till F_n."""
    if not 0 <= n <= 1000:
        return jsonify(error='n must between 0 and 1000'), 400
    t = time.time()
    return jsonify(n=n, seq=fib.seq(n), ms=(time.time() - t) * 1e3)

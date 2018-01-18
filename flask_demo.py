import time
import datetime

from flask import Flask
from flask import jsonify

app = Flask(__name__)

def fib_gen():
    """Fibonacci sequence generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

@app.route('/')
def index():
    """Welcomepage"""
    now = datetime.datetime.now().isoformat()
    return jsonify(message='Hello World!', ts=now)

@app.route('/fib/<int:n>')
def fib(n):
    """Get Fibonacci sequence till F_n."""
    if not 0 <= n <= 1000:
        return jsonify(error='n must between 0 and 1000'), 400
    t = time.time()
    fg = fib_gen()
    seq = [next(fg) for i in range(n + 1)]
    return jsonify(n=n, seq=seq, ms=(time.time() - t) * 1e3)

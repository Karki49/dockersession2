import logging
from flask import Flask, request

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

import random

employeeID = random.randint(100, 999)


@app.route('/resign')
def resign():
    logging.info("  I(employeeID:{0}) have resigned".format(employeeID))
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/whatdoyoudo')
def whatdoyoudo():
    return "\n  I create bugs and hope the QA finds it! (employeeID:%s)\n" % employeeID


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

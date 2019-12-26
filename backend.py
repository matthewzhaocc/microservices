import flask
import random
web = flask.Flask(__name__)
@web.route('/coinFlip')
def coinFlip():
    if random.randint(0,1) == 0:
        return 'tail'
    return 'head'

web.run(host='0.0.0.0',port=8000)
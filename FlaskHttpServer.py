from flask import Flask
app = Flask(__name__)
from flask import request
from flask import jsonify

@app.route('/test')
def hello():
    a = request.args.get('a',  type = int),
    b = request.args.get('b',  type= str )

    code = 0
    msg = 'success'
    res = ''
    if a is not None and a[0] is not None and b is not None:
        res = b
    else:
        code = 1
        msg = 'wrong params'
    return jsonify(
        code=code,
        msg=msg,
        res=res
    )

if __name__ == '__main__':
    app.run()
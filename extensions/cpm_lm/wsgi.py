# -*- coding: utf-8 -*-
from flask import Flask, jsonify, redirect, request, url_for
from datetime import datetime
import time
from sample import sample

app = Flask(__name__)


@app.route('/api/inference', methods=['POST'])
def inference():
    data = request.get_json()
    args = {}
    if 'length' in data:
        args['length'] = data['length']
    query = data['query']
    answer = sample(query, **args)[0]
    # answer = "DEBUG测试"
    return jsonify({
        'code': 200,
        'message': 'ok',
        'answer': answer
    })


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=6666)
    # app.run(debug=True, host='0.0.0.0', port=6666)

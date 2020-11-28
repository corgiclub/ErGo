# -*- coding: utf-8 -*-
from flask import Flask, jsonify, redirect, request, url_for
from datetime import datetime
from sample import sample

app = Flask(__name__)


@app.route('/api/inference', methods=['POST'])
def create_todo():
    data = request.get_json()

    args = {}
    if 'output_length_limit' in data:
        args['length'] = data['output_length_limit']
    query = data['content']
    answer = sample(query, **args)[0]
    return jsonify({
        'code': 200,
        'message': 'ok',
        'answer': answer
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6666)

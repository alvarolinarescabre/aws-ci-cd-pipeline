#!/usr/bin/env python3
import os
import time
from flask import Flask, jsonify

app = Flask(__name__)
START_TIME = time.time()


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'App funcionando correctamente en ECS'
    })


@app.route('/api/version', methods=['GET'])
def version():
    return jsonify({
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('APP_ENV', 'production')
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)

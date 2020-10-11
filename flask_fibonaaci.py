# !/usr/bin/python
# coding=UTF-8
# Written by Suma Kori <suma.kori93@gmail.com>, March 2020

"""This script is used to perform FibonacciSeries.

- author: Suma Kori
- e-mail: suma.kori93@gmail.com
"""

from flask import Flask, jsonify, request

from fibonacci import fibonacci_series

app = Flask(__name__)

@app.route('/fib/<int:num>', methods=['GET'])
def get_fibonacci(num):
    fibonacci_series.main(str(num))
    return jsonify({'result': fibonacci_series.main(num)})
    #return jsonify({'result': fibonacci_series.main(num)})

@app.route('/health/', methods=['GET'])
def get_health_info():
    return jsonify({'Emergency': 'Call emergency if you have breathing issues'})

if __name__ == '__main__':
    #print(fibonacci_series.main('-10'))
    app.run(debug=True)
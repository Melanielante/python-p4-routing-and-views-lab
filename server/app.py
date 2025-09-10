#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print (parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [str(i) for i in range(parameter)]
    return "\n".join(numbers) + "\n"


@app.route('/math/<int:num1>/<op>/<int:num2>')
def math(num1, num2, op):
    if op == "+":
        return str (num1 + num2)
    
    elif op == "-":
        return str(num1 - num2)
    elif op == "*":
        return str (num1 * num2)
    elif op == "div":
        return str(num1 / num2)
    elif op == "%":
        return str (num1 % num2)
    else:
        return "invalid operation"
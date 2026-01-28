#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:user>")
def print_string(user):
    print(user)
    return f"{user}"

@app.route("/count/<int:num>")
def count(num):
     result = ""
     for i in range(num):
        result += f"{i}\n"
     return result
@app.route('/math/<int:num>/<string:opt>/<int:num2>')
def math(num,opt,num2):
     if opt == '+':
        result = num + num2
     elif opt == '-':
         result = num - num2
     elif opt == '*':
         result = num * num2
     elif opt == '%':
         result = num % num2
     elif opt == 'div': 
         result = num / num2
     else:
         return 0
     return str(result)
if __name__ == '__main__':
    app.run(port=5555, debug=True)

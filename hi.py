from flask import Flask
from flask_ask import Ask,statement,question,session,convert_errors
import json
import requests
import time
import unidecode


app = Flask(__name__)
ask = Ask(app, "/hello")



@app.route('/')
def homepage():
    return "Welcome to Mahesh World"

@ask.launch
def start_skill():
    welcome_messege='Welcome to mahesh '
    return question(welcome_messege)

name=''
@ask.intent("hello",convert={'name':name})
def hello(name):
    bye_text='welocome to {} World '.format(name)
    return statement(bye_text)

if __name__ == '__main__':
    app.run(debug=True)
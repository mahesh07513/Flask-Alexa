from flask import flask
from flask_ask import Ask, statement,question


app=Flask(__name__)
ask=Ask(app,"/mahesh")



@app.route('/')
def homepage():
	return "its works fine ."


@ask.launch
def startPoint():
	return statement("welcome to mahesh world")


if __name__ == '__main__':
	app.run(debug=True)
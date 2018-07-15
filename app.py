from flask import Flask
app = Flask(__name__)

def f(a,b):
	"""
	return the sum of 2 numbers or the combination of two strings
	"""
	return a+b

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hi")
def hi():
    return "Hi World!"

if __name__ == '__main__':
   app.run(debug=True)
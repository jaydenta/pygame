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

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s is here' % username	

if __name__ == '__main__':
   app.run(debug=True)
from flask import Flask
app = Flask(__name__)

def add_func(a,b):
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

@app.route('/add/<int:num_a>/<int:num_b>')
def add(num_a,num_b):
    # Return sum of num_a and num_b
    return 'Sum of %d and %d is %d' % (num_a,num_b,add_func(num_a,num_b))		

if __name__ == '__main__':
   app.run(debug=True)
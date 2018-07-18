from flask import Flask
from flask import render_template

app = Flask(__name__)

def add_func(a,b):
	"""
	return the sum of 2 numbers or the combination of two strings
	"""
	return a+b

def multiply_func(a,b):
    """
    return the product of 2 numbers or the combination of two strings
    """
    return a*b

@app.route("/")
def hello_world():
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

@app.route('/multiply/<int:num_a>/<int:num_b>')
def multiply(num_a,num_b):
    # Return sum of num_a and num_b
    return 'Product of %d and %d is %d' % (num_a,num_b,multiply_func(num_a,num_b))

@app.route('/pygame/<game_name>')
def portfolio(game_name):
    return render_template('index.html',a=game_name)

@app.route('/plot')
def plot():
    return render_template('plot.html')

if __name__ == '__main__':
   app.run(debug=True)
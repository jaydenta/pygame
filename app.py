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

def add_number_list(l):
    """
    l is a list variable, should be either a list of number
    or list of string
    This function should return the sum of all numbers or
    the combination of all the strings
    """

    result = 0
    for item in l:
        result = result + item
    return result

def add_string_list(l):
    """
    l is a list variable, should be either a list of number
    or list of string
    This function should return the sum of all numbers or
    the combination of all the strings
    """
    
    result = ''
    for item in l:
        result = result + item
    return result

@app.route("/")
def root():
    return render_template('index.html')

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
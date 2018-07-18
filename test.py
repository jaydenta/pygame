import pytest
from app import *

def test_add_number():
	'''
	Check if f returns the sum of 2 number
	'''
	actual = add_func(1,2)
	expect = 3
	assert actual == expect

def test_combine_string():
	'''
	Check if f returns the combination of two strings
	'''
	actual = add_func('a','b')
	expect = 'ab'
	assert actual == expect

def test_multiply_number():
	'''check if f returns the product of 2 numbers'''
	actual = multiply_func(2,3)
	expect = 6
	assert actual == expect

#test_number()

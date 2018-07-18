import pytest
from app import *

def test_number():
	'''
	Check if f returns the sum of 2 number
	'''
	actual = add_func(1,2)
	expect = 3
	assert actual == expect

def test_string():
	'''
	Check if f returns the combination of two strings
	'''
	actual = add_func('a','b')
	expect = 'ab'
	assert actual == expect

#test_number()

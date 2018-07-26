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

def test_add_number_list():
    """
	check if function returns the sum of the list of integers
    """
    actual = add_number_list([1,2,3])
    expect = 6
    assert actual == expect

def test_add_string_list():
    """
   check if function returns the combined string from a list of smaller strings
    """

    actual = add_string_list(['Hi ','my love','!'])
    expect = 'Hi my love!'
    assert actual == expect

def test_multiply_number_string():
	"""
	check if function returns the product of the list of integers
	"""
	actual = multiply_number_list([2,4,6,8])
	expect = 384
	assert actual == expect

#test_number()

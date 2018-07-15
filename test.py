import pytest
from app import *

def test_number():
	actual = f(1,2)
	expect = 3
	assert actual == expect

def test_string():
	actual = f('a','b')
	expect = 'ab'
	assert actual == expect

#test_number()

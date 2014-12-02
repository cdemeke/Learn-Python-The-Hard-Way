from nose.tools import *
from ex48 import parser


def test_Sentence():
	
	result = parser.Sentence(('noun','bear'),('verb','eat'),('direction','east'))
	assert_equal(result.subject,'bear')
	assert_equal(result.verb,'eat')
	assert_equal(result.object,'east')
	
def test_peek():
	s1 = [('noun', 'bear'), ('verb', 'kill'), ('direction', 'north')]
	p1 = parser.peek(s1)
	p2 = parser.peek(s1)
	assert_equal =(p1, 'noun')
	assert_equal = (p2, 'noun')
   
def test_match():
   pass

def test_skip():
    pass

def test_parse_verb():
    pass

def test_parse_object():
    pass

def test_parse_subject():
    pass

def test_parse_sentence():
	pass
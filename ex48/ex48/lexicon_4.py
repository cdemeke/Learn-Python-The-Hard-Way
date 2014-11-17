lexicon = {
	'north'       : 'direction',
	'south'       : 'direction',
	'east'        : 'direction',
	'west'        : 'direction',
	'go'          : 'verb',
	'kill'        : 'verb',
	'eat'         : 'verb',
	'the'         : 'stop',
	'in'          : 'stop',
	'of'          : 'stop',
	'bear'        : 'noun',
	'princess'    : 'noun',
	1234          : 'number',
	3             : 'number',
	91234         : 'number',
    'asdfadfasdf' : 'error',
    'ias'         : 'error'
	}

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return s
        
# Find another way to convert the number.

def anotherway_convert_number(s):
	if s == int(s)
		return int(s)
	else 
		return s

def scan (sentence):
	words = sentence.lower()
	words = words.split()
	#words.lower()
	result = []

	for word in words:
		word = anotherway_convert_number(word) # checks if its a #
		pair = (lexicon[word], word)
		result.append(pair)

	return result



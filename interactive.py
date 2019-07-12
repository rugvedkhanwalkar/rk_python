import json
from difflib import get_close_matches
data = json.load(open('data.json'))
word_list = list(data.keys())
#word_match = data[word]
def translate(word):
    word = word.lower()
    #return(data[word])
    match_word = get_close_matches(word,word_list)
    #print(match_word)
    if word in data.keys():
        return (data[word])
    elif len(match_word)> 0:
	
	word_match = match_word[0]
	return(data[word_match])
    else:
	print('please try a valid word!')

#print(translate('rAinn'))

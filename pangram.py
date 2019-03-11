def is_pangram(sentence):
	sentence = sentence.lower()

	letters = ["a", "b", "c", "d", "e", "f" , "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	flag = 0
	for letter in letters:
	
		if letter in sentence:
			continue
		else:
			flag = 1
	if flag == 1 :
		return (False)
	else:
		return (True)

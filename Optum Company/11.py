'''
In a given String return the most frequent vowel coming.
'''

def most_frequent_vowel(string):
	string = string.lower()
	hashmap = {'a':0,'e':0,'i':0,"o":0,"u":0}
	for letter in string:
		if hashmap.get(letter)!=None:
			hashmap[letter]+=1
	max_freq = 0
	max_freq_vowel = None

	for letter in hashmap:
		if hashmap[letter] > max_freq:
			max_freq = hashmap[letter]
			max_freq_vowel = letter


	return max_freq_vowel


print(most_frequent_vowel("I love icecream"))

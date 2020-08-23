# https://practice.geeksforgeeks.org/problems/word-break/0
def solve_string(dictionary,output_string,current_string,i=0):
	
	#if we found full match
	if current_string == output_string:
		return 1

	#for all words start with ith letter in output_string.....(In case if we theres no words starting with ith letter return empty list)
	for word in dictionary.get(output_string[i],[]):
		#get the length
		l = len(word)
		
		#print((current_string+word),output_string[:i+l])
		#if word fits with current string (for eg:  i+like == ilikesamsung[:i+l])
		if (current_string+word) == output_string[:i+l]:
			#if we found full match 
			if (solve_string(dictionary,output_string,current_string+word,i+l)):
				return 1

	return 0

#Driver program - Test cases
T = int(input())
for _ in range(T):

	#get inputs
    N = int(input())
    dictionary_words = input().split()
    output_string = input()
    
    #convert dictionary words into dictonary
    '''
    something like this
	
	input_dictionary = "i like sam sung samsung mobile ice cream, icecream man go mango"
	
	is converted to 

	d = {'i': ['i', 'ice', 'icecream'], 'l': ['like'], 's': ['sam', 'sung', 'samsung'], 'm': ['mobile', 'man', 'mango'], 'c': ['cream,'], 'g': ['go']}
    '''
    d = {}
    for word in dictionary_words:
    	if not d.get(word[0]):
    		d[word[0]] = [word]
    	else:
    		d[word[0]].append(word)
    #print(d)

    print(solve_string(d,output_string,'',0))
    

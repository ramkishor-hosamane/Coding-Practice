'''

Find the occurrences of a digit d in a given range from 0 to n

'''

def get_occurences_digit(d,n):
	d =  str(d)
	count = 0
	for number in range(n+1):
		count+= list(str(number)).count(d)

	return count


print(get_occurences_digit(2,22))

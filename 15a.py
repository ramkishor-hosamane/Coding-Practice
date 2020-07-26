'''
Given a List of 10 numbers. Write the algorithm for creating another list of the same set of 10
numbers but rearranged such that all the numbers which are multiples of 2 are to the left of all the
numbers which are not multiples of 2.
'''
def solve(array,n):
	result = [0 for i in range(n)]
	j=0
	k=1
	for i in range(n):
		if(array[i]%2==0):
			result[j] = array[i]
			j+=2
		else:
			result[k]=array[i]
			k+=2			

	return result

array = [1,4,5,2,3,6,7,9,8,10]
n = len(array)

print(solve(array,n))
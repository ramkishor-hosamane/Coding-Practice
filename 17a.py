'''
Given a list of 10 numbers. Write an algorithm for creating another list of the same set of 10
numbers such that the numbers which occupy the “odd” positions in the first list are put in the first
half of the new list and those which occupy the “even” positions in the first list are put in the second
half of the new list without altering their relative order.
'''
def solve(array,n):
	result = [0 for i in range(n)]
	j=0
	for i in range(0,n,2):
		result[j] = array[i]
		j+=1
	for i in range(1,n,2):
		result[j] = array[i]
		j+=1
	


	return result

array = [1,4,5,2,3,6,7,9,8,10]
n = len(array)

print(solve(array,n))
'''
To check if numbers at even indices of an array were even or not.
'''
def check_even_indices(array,n):
	for i in range(0,n,2):
		if array[i] % 2:
			print(f"Number {array[i]} is present at {i}th position is odd")
			return

	print("All numbers at even indices are even")


a = [0,1,2,3,4,5,6,7,10]
check_even_indices(a,len(a))
def rotate(array):
	#Rotate the array by 1 element clockwise

	# get the last element
	x = array.pop()
	#insert x at the first position
	array.insert(0,x)


def solve(array,n):
	N=n
	# iterate n-1 times
	for k in range(1,n):
		#roate array (since array(list in python) is mutable changes made in other function will take effect)
		rotate(array)
		print(array)
		
		# caluculate index to be deleted
		index = (N-k)
		if index<0:
			index = 0
		array.pop(index)
		# decrease the size of the array 
		N-=1
	print("Array element left is ",array[0])



# test cases
array = [1 ,2 ,3 ,4, 5, 6]
array = [1 ,2 ,3 ,4]
array= list(range(1,111))

solve(array,110)
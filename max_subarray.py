# https://practice.geeksforgeeks.org/problems/maximum-sub-array/0
def Max_Subarray(array,n):
	prev_start = 0
	prev_sum = 0
	prev_length = 0
	prev_end = 0
	i = 0

	while i < n:
		start = i
		end = i
		Sum = 0
		while i < n and array[i]>=0:
			end+=1
			Sum+=array[i]
			i+=1
		length = end-start
		update = False
		if Sum > prev_sum:
			update = True

		elif Sum == prev_sum:
			if length > prev_length:
				update  = True

		if update:
			prev_length = length
			prev_sum=  Sum
			prev_end = end
			prev_start = start
			sub_array = array[start:end]

		i+=1

	return sub_array


# Testcases
array = [1, 2, 5, -7, 2, 3]
array = [2, 4, 49, -7, 2, 3,50]
array = [-8, -4, 0, -1, -2, -3]

n = len(array)
print(Max_Subarray(array,n))

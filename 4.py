'''
4. N numbers ranging From 1 to N are given, there is exactly one number missing and
exactly one is repeated find the repeated and missing number.
'''

#solution 1
def find_duplicate1(arr,n):
	Sum =  n * (n+1)/2
	return sum(arr) - Sum

#solution 2
def find_duplicate2(arr,n):
	arr.sort()
	for i in range(1,n):
		if arr[i]==arr[i-1]:
			return arr[i]


#solution 3
def find_duplicate3(arr,n):
	h = {}
	for x in arr:
		if h.get(x):
			return x
		else:
			h[x] = x


a = [3,4,5,2,6,1,5]
print(find_duplicate3(a,6))


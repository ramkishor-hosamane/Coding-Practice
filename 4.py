'''
4. N numbers ranging From 1 to N are given, there is exactly one number missing and
exactly one is repeated find the repeated and missing number.
'''


#solution 3
def find_duplicate(arr,n):
	h = {x:0 for x in range(1,n+1,1)}
	for x in arr:
		h[x]+=1
	#print(h)

	for x in h:
		if h[x] == 2:
			print(x,"is repeated Twice")
			
		if h[x] == 0:
			print(x,"is the missing number")

a = [1,2,3,3]
find_duplicate(a,len(a))


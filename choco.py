def solve(array,n,m):
	array = sorted(array)
	m-=1

	res = array[m] - array[0]
	for i in range(m,n,1):
		#print(array[i],array[i-m])
		res = min(res,array[i]-array[i-m])


	return res



array = [3, 4 ,1 ,9 ,56, 7, 9 ,12]
array = "34 88 89 39 67 71 85 57 18 7 61 50 38 6 60 18 19 46 84 74 59"
array=list(map(int,array.split()))
#print(solve(array,21,12))




def Max_Subarray(array,n):
	print(array)
	h =  {}
	si = 0
	Sum = 0
	for i,x in enumerate(array):
		if x >=0:
			Sum+=x
			h[x] = (si,i,Sum)
		else:
			Sum = 0
			h[x] = (i,i,0)
			si = i + 1
	print(h) 


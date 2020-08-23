

def Intervals(I):
	I = [list(I[i:i+2]) for i in range(0,len(I),2)]
	I = sorted(I,key = lambda x: x[0])
	i = 1
	while i < len(I):

		if I[i][0] <= I[i-1][1]:
			I[i-1][0] = min(I[i-1][0],I[i][0])
			I[i-1][1] = max(I[i-1][1],I[i][1])

			I.pop(i)
		else:
			i+=1

	print(I)


I = [1,3,2,6,8,10,15,18]
I = [5,1,6,8,4,3,1,9]
Intervals2(I)
print(solve(5))




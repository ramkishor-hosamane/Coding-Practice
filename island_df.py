def search(a,n,row,col):
	if(row>=0 and row<n and col>=0 and col<n and a[row][col]==1):
		a[row][col]=2
		search(a,n,row+1,col)
		search(a,n,row-1,col)
		search(a,n,row,col+1)
		search(a,n,row,col-1)

		#search(a,n,row+1,col+1)
		#search(a,n,row-1,col-1)
		#search(a,n,row+1,col-1)
		#search(a,n,row-1,col+1)


def solve(a,n):
	res=0
	for i in range(n):
		for j in range(n):
			if a[i][j]==1:
				res+=1
				search(a,n,i,j)
	return res


a = [
		[1,1,0,0,0],
		[0,1,0,0,1],
		[1,0,0,1,1],
		[0,0,0,0,0],
		[1,0,1,0,1]
		
	]

#output : 5
print(solve(a,5))
def search(a,n,row,col,queue):
	if(row>=0 and row<n and col>=0 and col<n and a[row][col]==1):
		a[row][col]=2
		queue.insert(0,(row+1,col))
		queue.insert(0,(row-1,col))
		queue.insert(0,(row,col+1))
		queue.insert(0,(row,col-1))
		queue.insert(0,(row+1,col+1))
		queue.insert(0,(row-1,col-1))
		queue.insert(0,(row+1,col-1))
		queue.insert(0,(row-1,col+1))


def bfs(a,n,queue):
	while queue!=[]:
		row,col = queue.pop()
		search(a,n,row,col,queue)

def solve(a,n):
	res=0
	queue = []
	for i in range(n):
		for j in range(n):
			if a[i][j]==1:
				res+=1
				queue.insert(0,(i,j))
				bfs(a,n,queue)
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
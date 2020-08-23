# https://practice.geeksforgeeks.org/problems/swapping-pairs-make-sum-equal/0
def solve(a,b):
	sum_a = sum(a)
	sum_b = sum(b)
	diff = abs(sum_b-sum_a)
	h = {abs(diff-x):x for x in a}
	for x in b:
		if h.get(x,-10000)+x == diff:
			return 1

	return -1

'''T =  int(input())
for _ in range(T):
	N,M = list(map(int,input().split()))
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	ans = solve(a,b)
	print(ans)
'''
'''a = [4, 1 ,2 ,1 ,1 ,1]
b = [3, 6, 3, 3]
ans = solve(a,b)

print(ans)
'''


def solve(A,B,Res,subset=[]):
	if B<0:
		return
	elif B==0:
		Res.append(tuple(subset))
	for x in A:
		C = A.copy()
		C.remove(x)
		solve(C,B-x,Res,subset.append(x))


def combination_sum(A,B):
	A = sorted(A)
	Res = []
	for i,x in enumerate(A):
		solve(A[i:],B,Res)
	return Res

A = [10, 1, 2 ,7 ,6, 1 ,5]
B = 8

print(combination_sum(A,B))
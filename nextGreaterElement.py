def nextGreater(a,n):
    res = [0 for i in range(n)]
    stack=[]
    for i in range(n-1,-1,-1):
        while len(stack)>0 and a[i] > stack[-1]:
            stack.pop()
        if len(stack)==0:
            res[i] = -1
        else:
            res[i] = stack[-1]
        stack.append(a[i])
    for x in res:
        print(x,end=" ")
    print()
T = int(input())
for _ in range(T):
	N = int(input())
	a = list(map(int,input().split()))
	nextGreater(a,N)



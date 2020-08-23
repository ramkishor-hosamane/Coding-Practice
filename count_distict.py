# https://practice.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1

def countDistinct(arr, N, K):
    i = K
    
    h = dict()
    ans = 0
    for x in arr[:i]:
    	if h.get(x):
    		h[x]+=1
    	else:
    		h[x]=1
	    	ans+=1
    res = [ans]
    while i < N:


    	h[arr[i-K]] = h.get(arr[i-K],1) - 1
    	if h[arr[i-K]]==0:
    		h.pop(arr[i-K])
    		ans-=1

    	if not h.get(arr[i],None):
    		#print("executeed  ",h)
    		ans+=1
    		h[arr[i]]=1
    	else:
    		h[arr[i]]+=1
    	res.append(ans)
    	i+=1
    return res

a = [66, 60, 37, 33, 52, 38 ,29, 76, 8 ,75, 22 ,59, 96, 30, 38 ,36, 94, 19 ,29, 44, 12 ,29]    
K = 14
print(countDistinct(a,len(a),K))
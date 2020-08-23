
def is_pointing(L1,L2):
	h={} #hashmap
	
	cur = L1.head
	while cur!=None:
		h[cur]=cur

	cur = L2.head
	while cur.next!=None:
		if h.get(cur.next):
			print(f"{cur} pointing to {cur.next}")
			return True 
	print("Not pointing")
	return False


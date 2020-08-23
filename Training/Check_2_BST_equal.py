

def trav(node1,node2):
	if node1!=None and node2!=None:
		if node1.data == node2.data:
			trav(node1.left,node2.left)
			trav(node1.right,node2.right)
		else:
			return "No"
	else:
		return "No"

	return "Yes"	

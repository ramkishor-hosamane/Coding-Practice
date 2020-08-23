def find_shortest_path(graph,start,end,path):
	path = path + [start]
	if start == end:
		return path
	shortest = None 
	for node in graph[start]:
		if node not in path:
			new_path = find_shortest_path(graph,node,end,path)
			if new_path:
				if not shortest or  len(new_path)<len(shortest):
					shortest = new_path
	return shortest
			


g = {
		'a':['b'],
		'b':['a','c','e'],
		'c':['b','d'],
		'd':['c','g'],
		'e':['b','f','h'],
		'f':['e'],
		'g':['d','h'],
		'h':['e','g']
	}
g = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
path = []
print(find_shortest_path(g,1,3,path))
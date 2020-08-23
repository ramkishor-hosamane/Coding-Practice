def find_all_paths(graph, start, end,cost,all_paths,path=[],totalcost=0):
    path = path + [start]
    totalcost +=cost

    if start == end:
    	all_paths.=append((path,totalcost))
    	return
    if graph.get(start)==None:
    	return
    for node,Cost in graph[start]:
    	if node not in path:
        	find_all_paths(graph, node, end,Cost,all_paths, path,totalcost)


def solve(graph,From,To):
	all_paths = []
	find_all_paths(graph,From,To,0,all_paths)
	all_paths.sort(key=lambda x:x[1])
	print(all_paths)
	

#Testcase 1
graph = {	
			"Bengaluru":[("Coimbatore",10000),("Chennai",4000)],
			"Chennai":[("Coimbatore",4000)]
		 }
From,To = "Bengaluru","Coimbatore"


#Testcase 2
graph = {	
			"Bengaluru":[("Coimbatore",10000),("Chennai",4000)],
			"Chennai":[("Coimbatore",4000)]
		 }
From,To = "Bengaluru","Coimbatore"



paths =[]
solve(graph,From,To)
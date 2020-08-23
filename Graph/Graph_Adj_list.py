from collections import defaultdict
class Graph:
    def __init__(self,graph_dict=None,directed = False):
        if not graph_dict:
            graph_dict = defaultdict(list)
        self.graph_dict = graph_dict
        self.directed = directed

    def add_edge(self,node1,node2):
        self.graph_dict[node1].append(node2)
        if not self.directed:
            self.graph_dict[node2].append(node1)
    

    
    def find_path(self,path,node,end):
        path = path+[node]
        if node == end:
            return path
        for neighbor_node in self.graph_dict[node]:
            if neighbor_node not in path:
                newpath = self.find_path(path,neighbor_node,end)
                if newpath:
                    return newpath
        
        return None
        
    
    def get_vertices(self):
        return list(self.graph_dict.keys())
    def display_graph(self):
        print("Vertices are  ",self.get_vertices())
        print("Graph \n")
        for vertice in self.graph_dict:
            print(vertice," : ",self.graph_dict[vertice])


g = Graph(directed=True)
g.add_edge("0","4")
g.add_edge("4","3")
g.add_edge("3","2")
g.add_edge("2","1")
g.add_edge("1","4")
g.add_edge("4","5")
g.display_graph()

print(g.find_path([],"3","5"))
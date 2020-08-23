class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.adj_mat = [[0 for i in range(vertices)] for i in range(vertices)] 
        print(vertices)

    def add_edge(self,start,end):
        self.adj_mat[start][end] = 1
    
    def is_path(self,start,end):
        pass

    def display_graph(self):
        for v in self.adj_mat:
            for u in v:
                print(u,end=" ")
            print()

g = Graph(6)
g.add_edge(0,4)
g.add_edge(4,3)
g.add_edge(3,2)
g.add_edge(2,1)
g.add_edge(1,4)
g.add_edge(4,5)
g.display_graph()
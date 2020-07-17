from queue import Queue 

# Initializing a queue 
q = Queue(maxsize = 0) 

class GraphNode(object):  
    def __init__(self, index):
        self.name = None
        self.index = index
        self.neighbors = []
        self.is_visited = False
        self.parent = None

class PathFindingByBFS(object):
    def __init__(self, graph_nodes):
        self.graph_nodes = graph_nodes

    def path(self, graphNode):
        if graphNode.parent is not None:
            self.path(graphNode.parent)
        print(graphNode.index)
    
    def bfs_ssp(self, graphNode):
        q.put(graphNode)
        graphNode.is_visited = True

        while not q.empty():
            present_node = q.get()
            #presentNode.is_visited = True
            print(" ") #to identify the seprate paths
            self.path(present_node)
            
            for neighbhor in  present_node.neighbors:
                if not neighbhor.is_visited:
                    q.put(neighbhor)
                    neighbhor.is_visited = True
                    neighbhor.parent = present_node
	
    def add_undirected_edge(self, source_vertex, destination_vertex):
        first = self.graph_nodes[source_vertex]
        second = self.graph_nodes[destination_vertex]
        first.neighbors.append(second)
        second.neighbors.append(first)

def start_main():
    graph_nodes = []
        
    for i in range(10):
        graph_nodes.append(GraphNode(i))
        
    graph = PathFindingByBFS(graph_nodes)
    graph.add_undirected_edge(0,8)
    graph.add_undirected_edge(8,2)
    graph.add_undirected_edge(8,9)
    graph.add_undirected_edge(2,1)
    graph.add_undirected_edge(9,1)
    graph.add_undirected_edge(2,4)
    graph.add_undirected_edge(1,3)
    graph.add_undirected_edge(1,7)
    graph.add_undirected_edge(3,4)
    graph.add_undirected_edge(3,5)
    graph.add_undirected_edge(7,6)
    graph.add_undirected_edge(5,6)

    print("Printing BFS from source: 2")
    graph.bfs_ssp(graph_nodes[2])
    
if __name__ == "__main__":
    start_main()
    
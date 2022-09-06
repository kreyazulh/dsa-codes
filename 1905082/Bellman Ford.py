class Graph:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
        #print(self.graph)


    def print_solution(self, dist, dest):
        print("Shortest path cost: ", end="")

        for i in range(self.V):
            if(i==dest):
                print((dist[i]))

    def print_path(self, src, dest):

        if dest<0:
            return[]
        return self.print_path(src, src[dest])+[dest]



    def bellman_ford(self, src, dest):



        dist = [float("Inf")] * self.V
        dist[src]=src
        #print(src)
        source=[-1]*self.V
        #dist[src] = src



        for i in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                	source[d]=s
                	dist[d]=dist[s]+w
                	#print(" %d %d %d %d %d" %(s, d, w, dist[s], dist[d]))

                	#dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("The graph contains a negative cycle")
                return

        self.print_solution(dist, dest)
        p=self.print_path(source, dest)
        print(p[0],end=" ")
        for i in range(len(p)-1):
            print("-> %d" %p[i+1], end=" ")



m = list(map(str, input().split()))
g = Graph(int(m[0]))

for i in range(int(m[1])):
    x = list(map(str, input().split()))
    # print(x)
    g.add_edge(int(x[0]), int(x[1]), int(x[2]))

for i in range(1):
	x = list(map(str, input().split()))
	g.bellman_ford(int(x[0]), int(x[1]))

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]

    def add_edge(self, node1, node2, weight):
        self.graph[node1][node2] = weight
        #self.graph[node2][node1] = weight

    def minDistance(self, dist, queue):
        minimum = float("Inf")
        min_index = -1

        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index


    def printPath(self, parent, j):

        if parent[j] == -1:
            print(j, end="")
            return
        self.printPath(parent, parent[j])
        print(" -> %d" %j, end="")

    def printSolution(self, dist, parent, dest):
        src = 0
        print("Shortest path cost: ", end="")
        for i in range(1, len(dist)):
            if i==dest:
                print("%d" % (dist[i]))
                self.printPath(parent, i)


    def dijkstra(self, src, dest):

        row = len(self.graph)
        col = len(self.graph[0])

        dist = [float("Inf")] * row


        parent = [-1] * row


        dist[src] = 0

        queue = []
        for i in range(row):
            queue.append(i)


        while queue:


            u = self.minDistance(dist, queue)


            queue.remove(u)

            for i in range(col):

                if self.graph[u][i] and i in queue:
                    if dist[u] + self.graph[u][i] < dist[i]:
                        dist[i] = dist[u] + self.graph[u][i]
                        parent[i] = u

        self.printSolution(dist, parent, dest)



m = list(map(str, input().split()))
g = Graph(int(m[0]))

for i in range(int(m[1])):
    x = list(map(str, input().split()))
    # print(x)
    g.add_edge(int(x[0]), int(x[1]), int(x[2]))

for i in range(1):
	x = list(map(str, input().split()))
	g.dijkstra(int(x[0]), int(x[1]))

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]

    def add_edge(self, node1, node2, weight):
        self.graph[node1-1][node2-1] = weight
        #self.graph[node2-1][node1-1] = weight
        #print(self.graph[0][1])
        #print(self.V)


    def floyd_warshall(self):
        INF=99999
        for i in range(self.V):
            for j in range(self.V):
                if i!=j and self.graph[i][j]==0:
                    self.graph[i][j]=INF
        #print(self.graph)
        distance = list(map(lambda i: list(map(lambda j: j, i)), self.graph))
        #print(distance)
        # Adding vertices individually
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        self.print_solution(distance)

    def print_solution(self,distance):
        print("Shortest distance matrix")
        for i in range(self.V):
            for j in range(self.V):
                if (distance[i][j] == 99999):
                    print("INF", end=" ")
                else:
                    print(distance[i][j], end="  ")
            print(" ")


m = list(map(str, input().split()))
g = Graph(int(m[0]))
for i in range(int(m[1])):

    x =list(map(str, input().split()))
    #print(x)
    g.add_edge(int(x[0]),int(x[1]), int(x[2]))


g.floyd_warshall()
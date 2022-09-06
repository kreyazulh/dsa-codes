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

    def matrix_mult_paths(self):
        INF=99999
        for i in range(self.V):
            for j in range(self.V):
                if i!=j and self.graph[i][j]==0:
                    self.graph[i][j]=INF
        #print(self.graph)
        distance = list(map(lambda i: list(map(lambda j: j, i)), self.graph))
        distance_square = list(map(lambda i: list(map(lambda j: j, i)), self.graph))
        #print(distance)
        # Adding vertices individually
        for m in range(2, self.V+1):
            #print(m)
            distance_square= self.matrix_mult(distance, distance_square)




        self.print_solution(distance_square)

    def matrix_mult(self, distance, distance_square):
        INF = 99999
        for i in range(self.V):
            for j in range(self.V):
               if i != j and distance_square[i][j] == 0:
                    distance_square[i][j] = INF

        for i in range(self.V):
            for j in range(self.V):

                for k in range(self.V):
                    #print(i)
                    distance_square[i][j] = min(distance_square[i][j], distance_square[i][k] + distance_square[k][j])
                    #print(distance_square)
        return distance_square


    def print_solution(self,distance_square):
        #print(distance_square)
        print("Shortest distance matrix")
        for i in range(self.V):
            for j in range(self.V):
                if (distance_square[i][j] == 99999):
                    print("INF", end=" ")
                else:
                    print(distance_square[i][j], end="  ")
            print(" ")


m = list(map(str, input().split()))
g = Graph(int(m[0]))
for i in range(int(m[1])):

    x =list(map(str, input().split()))
    #print(x)
    g.add_edge(int(x[0]),int(x[1]), int(x[2]))


g.matrix_mult_paths()
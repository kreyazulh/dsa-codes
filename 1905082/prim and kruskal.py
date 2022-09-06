class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.m_graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]


    def add_edgeK(self, u, v, w):
        self.graph.append([u, v, w])

    def add_edgeP(self, node1, node2, weight):
        self.m_graph[node1][node2] = weight
        self.m_graph[node2][node1] = weight


    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)

        w=0
        for u, v, weight in result:
            w=weight+w

        print("Cost of minimum spanning tree: ", end="")
        print(w)

        print("List of edges selected by Kruskal's: ", end="")
        print("{", end="")
        for u, v, weight in result:
            #print(weight, end=" ")
            print("(%d , %d)" % (u, v), end=",")
        print("}")



    #Prim's algorithm
    def prims_mst(self):
        postitive_inf = float('inf')

        selected_nodes = [False for node in range(self.V)]

        result = [[0 for column in range(self.V)]
                  for row in range(self.V)]

        indx = 0

        while (False in selected_nodes):

            minimum = postitive_inf
            start = 0
            end = 0

            for i in range(self.V):

                if selected_nodes[i]:
                    for j in range(self.V):
                        if (not selected_nodes[j] and self.m_graph[i][j] > 0):
                            if self.m_graph[i][j] < minimum:

                                minimum = self.m_graph[i][j]
                                start, end = i, j

            selected_nodes[end] = True
            result[start][end] = minimum

            if minimum == postitive_inf:
                result[start][end] = 0

            indx += 1

            result[end][start] = result[start][end]

        r=0
        print("List of edges selected by Prim's: ", end="")
        print("{", end="")
        for i in range(len(result)):
            for j in range(0 + i, len(result)):
                if result[i][j] != 0:
                    #print(result[i][j], end=" ")
                    print("(%d , %d)" % (i, j), end=",")
                    r=r+result[i][j]
        print("}")
        #print(r)




'''m = list(map(str, input().split()))
g = Graph(int(m[0]))

for i in range(int(m[1])):
    x = list(map(str, input().split()))
    # print(x)
    g.add_edgeK(int(x[0]), int(x[1]), float(x[2]))
    g.add_edgeP(int(x[0]), int(x[1]), float(x[2]))

g.kruskal_algo()
g.prims_mst()'''

with open("mst.in.txt",'r') as fin:
    for line in fin:
        m = line.split()
        break
g = Graph(int(m[0]))

with open('mst.in.txt', 'r') as fin:
    next(fin)
    for line in fin:
        x=line.split()
        g.add_edgeK(int(x[0]), int(x[1]), float(x[2]))
        g.add_edgeP(int(x[0]), int(x[1]), float(x[2]))

g.kruskal_algo()
g.prims_mst()




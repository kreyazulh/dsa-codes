from collections import defaultdict
from heapq import *
import timeit

class binary_heap:

    def dijkstra(edges, f, t):
        g = defaultdict(list)
        for l, r, c in edges:
            g[l].append((c, r))
            g[r].append((c,l))
        #print(g)


        q, seen, mins = [(0, f, [])], set(), {f: 0}
        while q:
            (cost, v1, path) = heappop(q)
            if v1 not in seen:
                seen.add(v1)
                path = [v1] + path
                if v1 == t:
                    return (cost, len(path))

                for c, v2 in g.get(v1, ()):
                    if v2 in seen:
                        continue
                    prev = mins.get(v2, None)
                    next = cost + c
                    if prev is None or next < prev:
                        mins[v2] = next
                        heappush(q, (next, v2, path))

        return (float("inf"), [])



class fibonacci_heap:
    def fibonacci(self, edges, N, source, dest):
        source -= 1
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u - 1].append((v - 1, w))
            graph[v - 1].append((u - 1, w))




        nodes = [None] * N

        class node:
            def __init__(self, i, value):
                self.i = i
                self.val = value
                self.degree = 0
                self.left = self
                self.right = self
                self.parent = None
                self.child = None
                self.visited = False
                nodes[i] = self

        def addNode(nd, dbn):  # dbn for 'a node in the double-linked list'
            nd.left = dbn.left
            dbn.left.right = nd
            nd.right = dbn
            dbn.left = nd

        def heapPush(nd):
            addNode(nd, self.minNode)

        def removeNode(nd):
            nd.left.right = nd.right
            nd.right.left = nd.left

        def heapPop():
            ret = (self.minNode.i, self.minNode.val)
            mnd = self.minNode
            if mnd.child:
                cur = mnd.child
                while cur:
                    child = cur
                    cur.parent = None
                    removeNode(cur)
                    cur = None if cur.right == cur else cur.right
                    heapPush(child)
                    # addNode(nd, self.minNode) to count nodes
            removeNode(mnd)
            self.minNode = mnd.right
            A = [None] * N
            while self.minNode:
                x = self.minNode
                removeNode(x)
                self.minNode = None if x.right == x else x.right
                x.left = x.right = x
                d = x.degree
                while A[d]:
                    y = A[d]
                    if x.val > y.val:
                        x, y = y, x
                    removeNode(y)
                    if x.child:
                        addNode(y, x.child)
                    else:
                        x.child = y
                    y.parent = x
                    x.degree += 1
                    y.visited = False
                    A[d] = None
                    d += 1
                A[d] = x
            for nd in A:
                if nd:
                    if self.minNode:
                        heapPush(nd)
                        # addNode(nd, self.minNode) to count nodes
                        if nd.val < self.minNode.val:
                            self.minNode = nd
                    else:
                        self.minNode = nd
            self.nodeCount -= 1
            return ret

        def cut(child, parent):
            parent.degree -= 1
            parent.child = None if child.right == child else child.right
            child.parent = None
            removeNode(child)
            child.left = child.right = child
            child.visited = False
            heapPush(child)
            #addNode(nd, self.minNode) to count nodes


        def cascadingCut(parent):
            pp = parent.parent
            if pp:
                if parent.visited:
                    cut(parent, pp)
                    cascadingCut(pp)
                else:
                    parent.visited = True

        def decrease(node, w):

            node.val = w
            parent = node.parent
            if parent and parent.val > node.val:
                cut(node, parent)
                cascadingCut(parent)
            if node.val < self.minNode.val:
                self.minNode = node

        dist = [float('inf')] * N
        dist[source] = 0
        prev = [None] * N
        self.minNode = node(source, 0)
        for i in range(N):
            if i != source:
                heapPush(node(i, dist[i]))
        self.nodeCount = N
        while self.nodeCount:
            source, w = heapPop()

            for d, t in graph[source]:
                alt = w + t
                if alt < dist[d]:
                    dist[d] = alt
                    prev[d] = source  # recording the path
                    decrease(nodes[d], alt)

        return -1 if dist[dest-1] == float('inf') else dist[dest-1]



if __name__ == "__main__":

    o = fibonacci_heap()
    path=[]
    result_bh=[]
    result_fh=[]
    time_bh=[]
    time_fh=[]



    with open("graph.txt", 'r') as fin:
        for line in fin:
            m = line.split()
            break

    edges=[]

    with open('graph.txt', 'r') as fin:
        next(fin)
        for line in fin:
            x = line.split()
            edges.append([int(x[0]), int(x[1]), int(x[2])])

    with open('pairs.txt', 'r') as fin:
        next(fin)
        for line in fin:
            x = line.split()

            start = timeit.default_timer()

            #print(binary_heap.dijkstra(edges, int(x[0]), int(x[1])))
            result_bh.append(binary_heap.dijkstra(edges, int(x[0]), int(x[1]))[0])
            path.append(binary_heap.dijkstra(edges, int(x[0]), int(x[1]))[1])

            stop = timeit.default_timer()
            execution_time = stop - start
            time_bh.append(execution_time*1000)

            #print(path)

            #print(time_bh)



            start2 = timeit.default_timer()

            print(o.fibonacci(edges, int(m[0]), int(x[0]), int(x[1])))
            result_fh.append(o.fibonacci(edges, int(m[0]), int(x[0]), int(x[1])))

            stop2 = timeit.default_timer()
            execution_time2 = stop2 - start2
            time_fh.append(execution_time2*1000)

            #print(time_fh)

    f = open("output.txt", "w")
    for i in range(len(path)):
        f.write(str(path[i]-1) +"    "+ str(result_fh[i])+"    "+str(time_bh[i])+"    "+str(time_fh[i])+ "\n")

    f.close()

    #for i in range(len(path)):
        #print(str(path[i]-1) +"    "+ str(result_fh[i])+"    "+str(time_bh[i])+"    "+str(time_fh[i]))
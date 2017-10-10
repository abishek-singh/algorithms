#! /usr/bin/env python2

from collections import defaultdict

class Graph(object):
    def __init__(self, V, directed=True):
        self.V = V
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def _bfs(self, u, visited):
        visited[u] = True
        queue = []
        queue.append(u)

        while queue:
            temp = queue.pop(0)
            print temp,
            for v in self.graph[temp]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True

    def bfs(self):
        visited = [False] * self.V

        for i in xrange(self.V):
            if not visited[i]:
                self._bfs(i, visited)

    def _dfs(self, u, visited):
        print u,
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self._dfs(v, visited)

    def dfs(self):
        visited = [False] * self.V

        for i in xrange(self.V):
            if not visited[i]:
                self._dfs(i, visited)

    def mother_vertex(self):
        visited = [False] * self.V
        mother = 0

        for i in xrange(self.V):
            if not visited[i]:
                self._dfs(i, visited)
                mother = i
        print
        visited = [False] * self.V
        self._dfs(mother, visited)
        print
        if any(i == False for i in visited):
            return -1
        return mother

    def _transitiveClosure(self, u, v, tc):
        tc[v][u] = 1

        for i in self.graph[u]:
            if not tc[v][i]:
                self._transitiveClosure(i, v, tc)

    def transitiveClosure(self):
        tc = [[0 for i in xrange(self.V)] for j in xrange(self.V)]

        for i in xrange(self.V):
            if not tc[i][i]:
                self._transitiveClosure(i, i, tc)

        return tc
        
    def _kCores(self, u, visited, k, vdegree):
        visited[u] = True

        for v in self.graph[u]:
            if vdegree[u] < k:
                vdegree[v] -= 1
            if not visited[v]:
                if self._kCores(v, visited, k, vdegree):
                    vdegree[u] -= 1

        return vdegree[u] < k

    def kCores(self, k):
        vdegree = [0] * self.V
        visited = [False] * self.V
        for i in self.graph:
            vdegree[i] = len(self.graph[i])
        
        for i in range(self.V):
            if not visited[i]:
                self._kCores(i, visited, k, vdegree)
        print "K-cores: "
        for v in range(self.V):
            if vdegree[v] >= k:
                print str("[ ") + str(v) + str(" ]"),
                for i in self.graph[v]:
                    if vdegree[i] >= k:
                        print "-> " + str(i),
                print


class Graph_Matrix(object):
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for i in range(self.V)] for j in range(self.V)]



if __name__ == "__main__":

    k = 3
    g1 = Graph (9, directed=False)
    g1.addEdge(0, 1)
    g1.addEdge(0, 2)
    g1.addEdge(1, 2)
    g1.addEdge(1, 5)
    g1.addEdge(2, 3)
    g1.addEdge(2, 4)
    g1.addEdge(2, 5)
    g1.addEdge(2, 6)
    g1.addEdge(3, 4)
    g1.addEdge(3, 6)
    g1.addEdge(3, 7)
    g1.addEdge(4, 6)
    g1.addEdge(4, 7)
    g1.addEdge(5, 6)
    g1.addEdge(5, 8)
    g1.addEdge(6, 7)
    g1.addEdge(6, 8)
    g1.kCores(k)
     
    g2 = Graph(13, directed=False)
    g2.addEdge(0, 1)
    g2.addEdge(0, 2)
    g2.addEdge(0, 3)
    g2.addEdge(1, 4)
    g2.addEdge(1, 5)
    g2.addEdge(1, 6)
    g2.addEdge(2, 7)
    g2.addEdge(2, 8)
    g2.addEdge(2, 9)
    g2.addEdge(3, 10)
    g2.addEdge(3, 11)
    g2.addEdge(3, 12)
    g2.kCores(k)

    #g.bfs()
    #g.dfs()
    #print "Mother Vertex: %s" % g.mother_vertex()

    #print "Transitive Closure"
    #tc = g.transitiveClosure()
    #for item in tc:
    #    for i in item:
    #        print i,
    #    print


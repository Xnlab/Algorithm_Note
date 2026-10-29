import sys
from collections import deque
input = sys.stdin.readline


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:        # 경로 압축 (반복문)
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        """합쳤으면 True, 이미 같은 그룹이면 False (사이클 판별에 사용)"""
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True


def kruskal(n, edges):
    """edges: (w, u, v). 반환: MST 총 비용 (연결 불가면 -1)"""
    uf = UnionFind(n)
    total = used = 0
    for w, u, v in sorted(edges):
        if uf.union(u, v):
            total += w
            used += 1
            if used == n - 1:
                break
    return total if used == n - 1 else -1


def topo_sort(n, edges):
    """edges: (u, v) = u가 v보다 먼저. 사이클이 있으면 []"""
    graph = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        cur = q.popleft()
        order.append(cur)
        for nxt in graph[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return order if len(order) == n else []


if __name__ == "__main__":
    uf = UnionFind(5)
    assert uf.union(0, 1) and uf.union(1, 2)
    assert not uf.union(0, 2)                 # 사이클
    assert uf.find(2) == uf.find(0) and uf.find(3) != uf.find(0)

    assert kruskal(3, [(1, 0, 1), (2, 1, 2), (3, 0, 2)]) == 3
    assert kruskal(4, [(1, 0, 1)]) == -1

    order = topo_sort(4, [(0, 2), (1, 2), (2, 3)])
    pos = {v: i for i, v in enumerate(order)}
    assert len(order) == 4 and pos[0] < pos[2] < pos[3] and pos[1] < pos[2]
    assert topo_sort(3, [(0, 1), (1, 2), (2, 0)]) == []
    print("07-union-find-mst OK")

import sys
import heapq
from collections import deque
input = sys.stdin.readline
INF = float("inf")


def dijkstra(graph, start):
    """graph[u] = [(v, w), ...] (w >= 0). 반환: start에서 각 노드까지 최단 거리"""
    dist = [INF] * len(graph)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, cur = heapq.heappop(pq)
        if d > dist[cur]:                # 이미 더 짧은 경로로 처리됨
            continue
        for nxt, w in graph[cur]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))
    return dist


def floyd_warshall(n, edges):
    """edges: (u, v, w) 방향 간선. 반환: dist[i][j]"""
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)  # 중복 간선 대비
    for k in range(n):                   # 경유지가 가장 바깥!
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                if dik + dk[j] < di[j]:
                    di[j] = dik + dk[j]
    return dist


def zero_one_bfs(graph, start):
    """graph[u] = [(v, w)], w는 0 또는 1"""
    dist = [INF] * len(graph)
    dist[start] = 0
    dq = deque([start])
    while dq:
        cur = dq.popleft()
        for nxt, w in graph[cur]:
            if dist[cur] + w < dist[nxt]:
                dist[nxt] = dist[cur] + w
                if w == 0:
                    dq.appendleft(nxt)
                else:
                    dq.append(nxt)
    return dist


if __name__ == "__main__":
    # 백준 1753 예제 (0-index)
    g = [[] for _ in range(5)]
    for u, v, w in [(5, 1, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (2, 4, 5), (3, 4, 6)]:
        g[u - 1].append((v - 1, w))
    assert dijkstra(g, 0) == [0, 2, 3, 7, INF]

    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1)]
    fw = floyd_warshall(4, edges)
    assert fw[0][1] == 3 and fw[0][3] == 4 and fw[3][0] == INF

    g01 = [[(1, 0), (2, 1)], [(2, 1), (3, 0)], [(3, 1)], []]
    assert zero_one_bfs(g01, 0) == [0, 0, 1, 0]
    print("06-shortest-path OK")

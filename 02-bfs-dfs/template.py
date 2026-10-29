import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start):
    """graph: 인접 리스트. 반환: start에서 각 노드까지 최단 거리 (도달 불가 -1)"""
    dist = [-1] * len(graph)
    dist[start] = 0
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:          # 넣을 때 방문 처리
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return dist


def grid_bfs(grid, starts, wall="#"):
    """격자 최단 거리. starts: 시작 좌표 리스트 (다중 시작 가능)"""
    n, m = len(grid), len(grid[0])
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    for r, c in starts:
        dist[r][c] = 0
        q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != wall and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist


def dfs_iterative(graph, start, visited):
    """반복문 DFS. 방문한 노드 수 반환 (연결 요소 크기)"""
    stack = [start]
    visited[start] = True
    size = 0
    while stack:
        cur = stack.pop()
        size += 1
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
    return size


def combinations_bt(n, k):
    """1..n 중 k개를 고르는 모든 조합 (백트래킹)"""
    result, path = [], []

    def go(start):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            go(i + 1)
            path.pop()               # 상태 원복

    go(1)
    return result


if __name__ == "__main__":
    g = [[1, 2], [0, 3], [0], [1], []]
    assert bfs(g, 0) == [0, 1, 1, 2, -1]

    maze = ["..#",
            ".#.",
            "..."]
    d = grid_bfs(maze, [(0, 0)])
    assert d[2][2] == 4 and d[0][2] == -1 and d[1][2] == 5

    visited = [False] * 5
    assert dfs_iterative(g, 0, visited) == 4
    assert sum(1 for v in range(5) if not visited[v] and dfs_iterative(g, v, visited)) == 1

    from itertools import combinations
    assert combinations_bt(5, 3) == [list(c) for c in combinations(range(1, 6), 3)]
    print("02-bfs-dfs OK")

import sys
from bisect import bisect_left
input = sys.stdin.readline
MOD = 1_000_000_007


def knapsack(items, cap):
    """items: (무게, 가치). 무게 cap 이하에서 최대 가치 (0/1 배낭)"""
    dp = [0] * (cap + 1)                 # dp[w] = 무게 w 이하로 얻는 최대 가치
    for w, v in items:
        for c in range(cap, w - 1, -1):  # 역방향! (각 물건 한 번만)
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[cap]


def lis_length(arr):
    """최장 증가 부분 수열 길이, O(n log n)"""
    tails = []                           # tails[k] = 길이 k+1인 증가 수열의 가장 작은 끝값
    for x in arr:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def lcs_length(a, b):
    """최장 공통 부분 수열 길이"""
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


def min_path_sum(grid):
    """왼쪽 위 → 오른쪽 아래, 오른쪽/아래로만 이동할 때 최소 합"""
    n, m = len(grid), len(grid[0])
    INF = float("inf")
    dp = [[INF] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for r in range(n):
        for c in range(m):
            if r > 0:
                dp[r][c] = min(dp[r][c], dp[r - 1][c] + grid[r][c])
            if c > 0:
                dp[r][c] = min(dp[r][c], dp[r][c - 1] + grid[r][c])
    return dp[n - 1][m - 1]


if __name__ == "__main__":
    assert knapsack([(6, 13), (4, 8), (3, 6), (5, 12)], 7) == 14
    assert lis_length([10, 20, 10, 30, 20, 50]) == 4
    assert lis_length([5, 4, 3]) == 1
    assert lcs_length("ACAYKP", "CAPCAK") == 4
    assert min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    print("05-dp OK")

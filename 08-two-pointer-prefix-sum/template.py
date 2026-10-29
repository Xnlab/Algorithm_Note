import sys
from collections import defaultdict
input = sys.stdin.readline


def build_prefix(arr):
    """prefix[i] = arr[0..i-1]의 합. 구간 [l, r] (0-index, 포함) 합 = prefix[r+1] - prefix[l]"""
    prefix = [0] * (len(arr) + 1)
    for i, x in enumerate(arr):
        prefix[i + 1] = prefix[i] + x
    return prefix


def build_prefix_2d(grid):
    """P[i][j] = grid[0..i-1][0..j-1]의 합"""
    n, m = len(grid), len(grid[0])
    P = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            P[i + 1][j + 1] = grid[i][j] + P[i][j + 1] + P[i + 1][j] - P[i][j]
    return P


def rect_sum(P, r1, c1, r2, c2):
    """(r1,c1) ~ (r2,c2) 직사각형 합 (0-index, 포함)"""
    return P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]


def min_len_sum_at_least(arr, s):
    """양수 배열에서 합이 s 이상인 가장 짧은 연속 구간 길이 (없으면 0)"""
    best = float("inf")
    total = left = 0
    for right, x in enumerate(arr):
        total += x
        while total >= s:
            best = min(best, right - left + 1)
            total -= arr[left]
            left += 1
    return 0 if best == float("inf") else best


def two_sum_sorted(arr, target):
    """정렬된 배열에서 합이 target인 쌍의 개수 (서로 다른 원소 가정)"""
    lo, hi, count = 0, len(arr) - 1, 0
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            count += 1
            lo += 1
            hi -= 1
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return count


def count_subarray_sum(arr, k):
    """합이 k인 연속 부분 배열 개수 (음수 포함 가능)"""
    seen = defaultdict(int)
    seen[0] = 1
    total = count = 0
    for x in arr:
        total += x
        count += seen[total - k]
        seen[total] += 1
    return count


if __name__ == "__main__":
    p = build_prefix([5, 4, 3, 2, 1])
    assert p[3] - p[0] == 12 and p[5] - p[1] == 10

    g = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
    P = build_prefix_2d(g)
    assert rect_sum(P, 1, 1, 2, 2) == 16 and rect_sum(P, 0, 0, 3, 3) == 64

    assert min_len_sum_at_least([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15) == 2
    assert min_len_sum_at_least([1, 1], 5) == 0

    assert two_sum_sorted([1, 2, 3, 5, 7, 9, 10, 11, 12], 13) == 3
    assert count_subarray_sum([1, -1, 1, 1], 1) == 5
    print("08-two-pointer-prefix-sum OK")

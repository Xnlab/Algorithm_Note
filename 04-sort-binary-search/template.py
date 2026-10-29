import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


def count_value(sorted_arr, x):
    """정렬된 배열에서 x의 개수"""
    return bisect_right(sorted_arr, x) - bisect_left(sorted_arr, x)


def count_range(sorted_arr, lo, hi):
    """정렬된 배열에서 lo <= v <= hi 인 값의 개수"""
    return bisect_right(sorted_arr, hi) - bisect_left(sorted_arr, lo)


def lower_bound(arr, x):
    """x 이상이 처음 나오는 인덱스 (bisect_left와 동일)"""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def max_feasible(lo, hi, ok):
    """ok(x)가 참인 가장 큰 x. ok는 [참...참, 거짓...거짓] 형태여야 함. 없으면 lo-1"""
    ans = lo - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if ok(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


def min_feasible(lo, hi, ok):
    """ok(x)가 참인 가장 작은 x. ok는 [거짓...거짓, 참...참] 형태여야 함. 없으면 hi+1"""
    ans = hi + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if ok(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans


if __name__ == "__main__":
    arr = [1, 2, 2, 2, 5, 7]
    assert count_value(arr, 2) == 3 and count_value(arr, 3) == 0
    assert count_range(arr, 2, 6) == 4
    for x in range(0, 9):
        assert lower_bound(arr, x) == bisect_left(arr, x)

    # 랜선 자르기: 길이 [802, 743, 457, 539]로 11개 → 최대 200
    cables, need = [802, 743, 457, 539], 11
    assert max_feasible(1, max(cables), lambda L: sum(c // L for c in cables) >= need) == 200

    # 입국심사: 심사관 [7, 10], 6명 → 최소 28분
    times, n = [7, 10], 6
    assert min_feasible(1, min(times) * n, lambda T: sum(T // t for t in times) >= n) == 28
    print("04-sort-binary-search OK")

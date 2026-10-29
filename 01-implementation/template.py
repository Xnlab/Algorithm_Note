import sys
input = sys.stdin.readline

# 4방향: 위, 오른쪽, 아래, 왼쪽 (시계 방향 순서 → d = (d + 1) % 4 가 오른쪽 회전)
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

# 8방향
DR8 = [-1, -1, 0, 1, 1, 1, 0, -1]
DC8 = [0, 1, 1, 1, 0, -1, -1, -1]


def in_range(r, c, n, m):
    return 0 <= r < n and 0 <= c < m


def rotate_cw(grid):
    """시계 방향 90도 회전 (n x m → m x n)"""
    return [list(row) for row in zip(*grid[::-1])]


def rotate_ccw(grid):
    """반시계 방향 90도 회전"""
    return [list(row) for row in zip(*grid)][::-1]


def turn_right(d):
    return (d + 1) % 4


def turn_left(d):
    return (d + 3) % 4


if __name__ == "__main__":
    g = [[1, 2, 3],
         [4, 5, 6]]
    assert rotate_cw(g) == [[4, 1], [5, 2], [6, 3]]
    assert rotate_ccw(g) == [[3, 6], [2, 5], [1, 4]]
    assert rotate_ccw(rotate_cw(g)) == g
    assert turn_right(3) == 0 and turn_left(0) == 3
    assert in_range(1, 2, 2, 3) and not in_range(2, 0, 2, 3)
    print("01-implementation OK")

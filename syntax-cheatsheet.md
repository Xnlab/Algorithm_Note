# Python 문법 치트시트 (코테용)

## 입력
```python
import sys
input = sys.stdin.readline          # 반드시! input()은 느림

n = int(input())
a, b = map(int, input().split())
arr = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
board = [input().rstrip() for _ in range(n)]   # 문자열은 개행 제거
```

## 출력
```python
print(*arr)                         # 공백으로 구분
print("\n".join(map(str, result)))  # 여러 줄을 한 번에 (print 반복보다 빠름)
```

## 재귀 깊이
```python
sys.setrecursionlimit(10**6)
```

## 정렬
```python
arr.sort()                          # 제자리
sorted(arr, reverse=True)           # 새 리스트
arr.sort(key=lambda x: (-x[1], x[0]))   # 두 번째 내림차순, 첫 번째 오름차순
```

## 자료구조
```python
from collections import deque, defaultdict, Counter
import heapq

q = deque(); q.append(x); q.popleft(); q.appendleft(x)

h = []; heapq.heappush(h, x); heapq.heappop(h)   # 최소 힙
heapq.heappush(h, -x); -heapq.heappop(h)          # 최대 힙
heapq.heappush(h, (cost, node))                   # 튜플은 첫 원소 기준

d = defaultdict(int); d[key] += 1
cnt = Counter(arr); cnt.most_common(1)

s = set(); s.add(x); x in s                       # 포함 여부 O(1)
```

## 이분탐색 · 조합
```python
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, product, accumulate

list(combinations(arr, 2))
list(permutations(arr, 2))
list(product([0, 1], repeat=3))
list(accumulate(arr))               # 누적합 (prefix[0] = 0 없음 주의)
```

## 수학
```python
from math import gcd, isqrt, inf
lcm = a * b // gcd(a, b)
isqrt(n)                            # 정수 제곱근
pow(a, b, mod)                      # 빠른 거듭제곱
divmod(a, b)                        # (몫, 나머지)
```

## 2차원 리스트
```python
grid = [[0] * m for _ in range(n)]  # O
grid = [[0] * m] * n                # X — 모든 행이 같은 객체
copy = [row[:] for row in grid]     # 깊은 복사 (2차원)
list(zip(*grid))                    # 전치
```

## 문자열
```python
s[::-1]                             # 뒤집기
"".join(lst)
ord("a"), chr(97)
s.isdigit(), s.isalpha()
```

## 성능 팁
- 함수 안에 코드를 넣으면 지역 변수 접근이 빨라진다 → `def main(): ...` 후 `main()`
- 큰 반복 안에서 `list.append`를 지역 변수로 빼두면 약간 빨라진다
- `in` 검사는 리스트 대신 `set`

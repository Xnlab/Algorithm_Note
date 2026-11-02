# 게임 개발

- **출처**: 이것이 취업을 위한 코딩 테스트다 with 파이썬 (나동빈) — Ch4 구현 실전 문제
- **유형**: 구현 (시뮬레이션)
- **푼 날짜**: 2026-11-02
- **결과**: 오답 (실행 불가 + 논리 오류)

## 문제 요약
바깥이 모두 바다인 N×M 맵에서 캐릭터가 "왼쪽으로 돌기 → 안 가본 육지면 전진, 아니면 다시 돌기 → 네 방향 모두 막히면 바라보는 방향 그대로 한 칸 뒤로, 뒤가 바다면 종료" 규칙을 반복할 때, 방문한 칸의 수를 구한다. 방향은 0 북, 1 동, 2 남, 3 서.

## 떠올렸어야 할 단서
- 규칙이 순서대로 나열되어 있음 → 알고리즘보다 **규칙을 그대로 옮기는 시뮬레이션**
- "왼쪽으로 회전" + 방향 번호가 **북 동 남 서(시계 방향)** 순서 → 왼쪽 회전은 `d - 1`
- "네 방향 모두" → 회전 횟수를 세거나, `for _ in range(4)`로 묶는다
- "바깥은 항상 바다" → 격자 범위 체크가 필요 없다는 신호

## 내 풀이

```python
n, m = map(int, input().split())
d = [[0] * for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def left():
    global direction
    direction -= -1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
```

- 시간복잡도: **O(N × M)** (각 칸은 한 번만 새로 방문하고, 칸마다 회전은 최대 4번)
- 평가: 전체 뼈대(방문 배열, 방향 벡터, 회전 횟수 `turn_time`, 뒤로 가기는 `x - dx`)는 책의 정석 풀이와 같다. 다만 아래 버그 때문에 실행되지 않고, 문법만 고쳐도 답이 틀린다.

### 버그 목록

| # | 위치 | 문제 | 결과 | 수정 |
|---|---|---|---|---|
| 1 | `[[0] * for ...]` | 곱할 값 `m`이 빠짐 | `SyntaxError` | `[[0] * m for _ in range(n)]` |
| 2 | `def left()` / `turn_left()` | 정의한 이름과 호출한 이름이 다름 | `NameError` | 둘 다 `turn_left` |
| 3 | `direction -= -1` | 1을 **더함** → 오른쪽으로 회전 | `direction`이 4가 되어 `IndexError` | `direction -= 1` |
| 4 | `dy = [0, -1, 0, 1]` | 1번이 서, 3번이 동이 됨 (문제는 1 동, 3 서) | 입력 방향과 실제 이동 방향이 어긋남 | `dy = [0, 1, 0, -1]` |
| 5 | 전진할 때 | 방문 표시만 하고 **캐릭터를 옮기지 않음** | 같은 자리에서 계속 회전 → 칸 수가 적게 나옴 | `x, y = nx, ny` 추가 |

### 버그별 영향 (직접 실행해서 확인)
- 1·2를 고친 뒤 3·4를 그대로 두면: 책 예제에서 `IndexError`
- 4만 남기면: 책 예제는 우연히 3으로 맞지만, 무작위 맵 19,757개 중 **7,213개 오답** (북→동으로 돌게 되어 사실상 오른쪽 회전)
- 5만 남기면: 책 예제에서 **2** (정답 3), 무작위 맵 중 **13,774개 오답**
- 3과 4는 짝을 이룬다: `dy`가 "북 서 남 동" 순서라면 `+1`이 왼쪽 회전이 되긴 하지만, 그러면 입력 방향(1 = 동)을 잘못 해석하고 `direction == -1` 대신 `== 4`를 확인해야 한다. **문제의 방향 번호를 그대로 쓰고 `-1`로 도는 게** 가장 안전하다.

### 1~5를 고친 버전 (원래 구조 유지)

```python
n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
```

## 개선된 풀이

```python
import sys
input = sys.stdin.readline

DR = [-1, 0, 1, 0]   # 0 북, 1 동, 2 남, 3 서 (문제의 번호 그대로)
DC = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
visited[r][c] = True
count = 1

while True:
    for _ in range(4):                       # 최대 네 방향 시도
        d = (d + 3) % 4                      # 왼쪽 회전 (= d - 1, 음수 없이)
        nr, nc = r + DR[d], c + DC[d]
        if board[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = True
            r, c = nr, nc
            count += 1
            break                            # 전진했으면 1단계부터 다시
    else:                                    # break 없이 4번 다 돌았다 = 네 방향 모두 막힘
        br, bc = r - DR[d], c - DC[d]        # 바라보는 방향 유지한 채 뒤로
        if board[br][bc] == 1:
            break
        r, c = br, bc

print(count)
```

- 시간복잡도: **O(N × M)**
- 바뀐 점
  - `turn_time` 카운터 대신 **`for _ in range(4)` + `for-else`**: 네 번 안에 `break`(전진)하지 않으면 `else`가 실행된다. "네 방향 모두 막힘"을 구조로 표현해서 카운터 초기화를 빼먹을 일이 없다.
  - `global`을 쓰는 회전 함수 대신 `d = (d + 3) % 4` 한 줄. `+3`은 `-1`과 같은 회전이지만 음수가 되지 않아 `if`로 보정할 필요가 없다.
  - 방향 배열을 **문제의 번호 순서 그대로** 두고 주석으로 표시 → 버그 4 같은 순서 실수를 막는다.
  - 방문 배열을 `True/False`로, 변수명을 `r, c`로 (행·열 혼동 방지)

## 검증
- 책 예제 (4×4, 시작 (1, 1) 북쪽) → 고친 버전·개선 버전 모두 `3`
- 3 ≤ N, M ≤ 9, 테두리는 바다인 무작위 맵 19,757개에서 고친 버전·개선 버전 모두 규칙을 문장 그대로 옮긴 기준 풀이와 결과 일치

## 배운 점
- 방향이 번호로 주어지면 **방향 배열 순서를 문제 번호에 맞추고**, 회전은 시계 방향 `(d + 1) % 4`, 반시계 방향 `(d + 3) % 4`로 외운다.
- 시뮬레이션에서는 "다음 위치 계산 → 조건 확인 → **실제로 이동**"의 세 단계 중 마지막을 자주 빼먹는다. 예제를 손으로 몇 단계 따라가 보면 바로 드러난다.
- "최대 k번 시도하고, 모두 실패하면 ~" 구조는 `for ... else`로 쓰면 카운터가 필요 없다.

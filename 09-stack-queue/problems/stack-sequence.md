# 스택으로 수열 만들기 (백준 1874 스택 수열)

- **출처**: Do it! 알고리즘 코딩테스트 with 파이썬 — 스택과 큐 / 백준 1874
- **유형**: 스택 (시뮬레이션)
- **푼 날짜**: 2026-11-17
- **결과**: 오답 (오타 한 군데로 실행 불가) — 고치면 정답

## 문제 요약
1부터 n까지의 수를 **오름차순으로만** 스택에 push할 수 있고, 아무 때나 pop할 수 있다. 주어진 수열(1 ~ n의 순열, n ≤ 100,000)을 pop 순서로 만들 수 있으면 push는 `+`, pop은 `-`로 연산 순서를 한 줄씩 출력하고, 불가능하면 `NO`를 출력한다.

## 떠올렸어야 할 단서
- "넣은 순서의 **역순**으로 꺼낸다" → 스택
- push는 1, 2, 3, … 순서로만 → 다음에 넣을 수를 변수 하나(`num`)로 관리
- 만들어야 하는 수가 **아직 안 넣은 수**면 그 수까지 push, **이미 넣은 수**면 스택 맨 위가 그 수여야만 pop 가능

## 내 풀이

```python
n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

stack = []
num = 1
result = True
answer = []

for i in range(n):
    su = a[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer.append('+')
        stack.pop()
        answer.append('-')
    else:
        p = stack.pop()
        if p > su:
            print("NO")
            return = False
            break
        else:
            answer.append('-')

if result:
    for i in answer:
        print(i)
```

- 시간복잡도: **O(N)** (각 수는 한 번 push, 한 번 pop)
- 평가
  - 논리는 책 풀이와 같고 정확하다.
  - **버그 1개**: `return = False` → `return`은 Python 예약어라 변수처럼 값을 넣을 수 없어 `SyntaxError`. 의도한 변수는 `result`.
  - `result = False`로 고치면 n = 1 ~ 6의 모든 순열(873개)에서 정답과 일치.

## 정답 풀이 (책 풀이 방식)

내 풀이에서 오타 한 군데만 고친 코드.

```python
n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

stack = []
num = 1                         # 다음에 push할 수
result = True                   # 수열을 만들 수 있는가
answer = []                     # + / - 기록

for i in range(n):
    su = a[i]                   # 이번에 꺼내야 하는 수
    if su >= num:               # 아직 안 넣은 수 → 그 수까지 push
        while su >= num:
            stack.append(num)
            num += 1
            answer.append('+')
        stack.pop()             # 맨 위가 su → 꺼냄
        answer.append('-')
    else:                       # 이미 넣은 수 → 맨 위에 있어야만 꺼낼 수 있음
        p = stack.pop()
        if p > su:              # 맨 위가 더 큰 수 → su는 그 아래에 묻혀 있음
            print("NO")
            result = False
            break
        else:
            answer.append('-')

if result:
    for i in answer:
        print(i)
```

## 해설

### 두 가지 경우
`num` = 다음에 push할 수 (지금까지 num − 1까지 넣었다)

| 꺼내야 할 수 su | 상황 | 동작 |
|---|---|---|
| su ≥ num | 아직 안 넣은 수 | num부터 su까지 push → 맨 위가 su → pop |
| su < num | 이미 넣은 수 | 맨 위를 pop. 그게 su면 성공, su보다 크면 **불가능** |

### 왜 맨 위가 su보다 크면 불가능한가
- 스택은 1, 2, 3, … 순서로 쌓이므로, 스택 안의 수는 **아래에서 위로 오름차순**이다.
- 맨 위 p가 su보다 크다 = su는 p보다 **아래**에 있다. su를 꺼내려면 p를 먼저 꺼내야 하는데, 그러면 수열 순서가 어긋난다.
- 맨 위가 su보다 작을 수는 없다. su는 이미 넣었고 아직 안 꺼냈으니 스택 안에 있고, 스택이 오름차순이라 맨 위는 su 이상이다. 그래서 `p > su`가 아니면 `p == su`다.

### `return = False`가 오류인 이유
- `return`, `if`, `for`, `while`, `True`, `None` 같은 **예약어**는 변수 이름으로 쓸 수 없다. 대입(`=`)의 왼쪽에 오면 바로 `SyntaxError`.
- 함수 밖에서 실행을 멈추고 싶다면 `return`이 아니라 지금처럼 `result` 같은 표시 변수 + `break`를 쓰거나, `exit()` / `sys.exit()`을 쓴다.
  ```python
  print("NO")
  sys.exit()        # 프로그램 즉시 종료 → result 변수 없이도 됨
  ```

### 예제 따라가기 (n = 8, 수열 4 3 6 8 7 5 2 1)

| su | num (전) | 동작 | 스택 (아래→위) | 기록 |
|---|---|---|---|---|
| 4 | 1 | 1~4 push, 4 pop | 1 2 3 | + + + + − |
| 3 | 5 | 맨 위 3 pop (= su) | 1 2 | − |
| 6 | 5 | 5~6 push, 6 pop | 1 2 5 | + + − |
| 8 | 7 | 7~8 push, 8 pop | 1 2 5 7 | + + − |
| 7 | 9 | 맨 위 7 pop | 1 2 5 | − |
| 5 | 9 | 맨 위 5 pop | 1 2 | − |
| 2 | 9 | 맨 위 2 pop | 1 | − |
| 1 | 9 | 맨 위 1 pop | (빈) | − |

`NO`가 되는 예: 수열 `1 2 5 3 4` → 5를 꺼낼 때 스택에 `3 4`가 남는다. 다음 su = 3인데 맨 위는 4 → 4 > 3 → **NO**.

### 입력·출력이 많을 때
- n이 10만이라 입력 10만 줄, 출력 최대 20만 줄이다. 로컬에서는 n = 100,000에 약 0.2초였지만, 습관적으로 다음을 쓰면 안전하다.
  ```python
  import sys
  input = sys.stdin.readline
  ...
  print('\n'.join(answer))      # 20만 번 print 대신 한 번에
  ```

## 검증
- 예제 1 → `+ + + + − − + + − + + − − − − −`, 예제 2 (`1 2 5 3 4`) → `NO`
- n = 1 ~ 6의 모든 순열 873개에서 기준 시뮬레이션과 일치
- n = 100,000 → 로컬 약 0.2초

## 배운 점
- **스택에 1부터 오름차순으로 넣으면 스택 안은 항상 오름차순** → 맨 위가 꺼낼 수보다 크면 불가능.
- 예약어(`return`, `if`, `for`, `True` …)는 변수 이름으로 쓸 수 없다. 오류 메시지가 `SyntaxError`면 철자·예약어부터 확인한다.
- 실행을 멈추는 방법: 함수 안이면 `return`, 반복문이면 `break`, 프로그램 전체면 `sys.exit()`.

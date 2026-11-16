# DNA 비밀번호 (백준 12891)

- **출처**: Do it! 알고리즘 코딩테스트 with 파이썬 — 슬라이딩 윈도우 / 백준 12891
- **유형**: 슬라이딩 윈도우
- **푼 날짜**: 2026-11-16
- **결과**: 정답 (책 풀이 방식)

## 문제 요약
A, C, G, T로 이루어진 길이 S(≤ 1,000,000)의 DNA 문자열에서, 길이 P인 **연속 부분 문자열** 중 A, C, G, T가 각각 **최소** 주어진 개수 이상 들어 있는 것의 개수를 구한다. 위치가 다르면 내용이 같아도 다른 것으로 센다.

## 떠올렸어야 할 단서
- "길이 P인 **연속** 부분 문자열"을 **모두** 확인 → 길이가 고정된 구간을 한 칸씩 미는 **슬라이딩 윈도우**
- S가 100만 → 구간마다 P개를 새로 세면 O(S × P) → 최대 수천억 → 불가능
- 한 칸 밀 때 바뀌는 건 **들어오는 문자 1개, 나가는 문자 1개**뿐 → 개수를 갱신만 하면 O(S)

## 내 풀이

```python
checklist = [0] * 4
mylist = [0] * 4
checksecret = 0

def myadd(c):
    global checklist, mylist, checksecret
    if c == 'A':
        mylist[0] += 1
        if mylist[0] == checklist[0]:
            checksecret += 1
    elif c == 'C':
        mylist[1] += 1
        if mylist[1] == checklist[1]:
            checksecret += 1
    elif c == 'G':
        mylist[2] += 1
        if mylist[2] == checklist[2]:
            checksecret += 1
    elif c == 'T':
        mylist[3] += 1
        if mylist[3] == checklist[3]:
            checksecret += 1

def myremove(c):
    global checklist, mylist, checksecret
    if c == 'A':
        if mylist[0] == checklist[0]:
            checksecret -= 1
        mylist[0] -= 1
    elif c == 'C':
        if mylist[1] == checklist[1]:
            checksecret -= 1
        mylist[1] -= 1
    elif c == 'G':
        if mylist[2] == checklist[2]:
            checksecret -= 1
        mylist[2] -= 1
    elif c == 'T':
        if mylist[3] == checklist[3]:
            checksecret -= 1 
        mylist[3] -= 1
    
s, p = map(int, input().split())
dna = list(input())
result = 0
checklist = list(map(int, input().split()))

for i in range(4):
    if checklist[i] == 0:
        checksecret += 1

for i in range(p):
    myadd(dna[i])

if checksecret == 4:
    result += 1

for i in range(p, s):
    j = i - p
    myadd(dna[i])
    myremove(dna[j])
    if checksecret == 4:
        result += 1
        
print(result)
```

- 시간복잡도: **O(S)** (문자마다 추가 1번, 제거 1번)
- 평가
  - 정답. 책 풀이와 같은 방식이다.
  - 조건을 만족한 문자 수를 `checksecret` 하나로 관리해서, 매 구간마다 네 문자를 다시 비교하지 않고 `checksecret == 4`만 확인한다.
  - 최소 개수가 0인 문자를 처음부터 "만족"으로 세어 둔 처리가 정확하다.

## 해설

### 변수 세 개의 역할

| 변수 | 뜻 |
|---|---|
| `checklist[k]` | 문자 k(0 A, 1 C, 2 G, 3 T)의 **필요한 최소 개수** (입력) |
| `mylist[k]` | 지금 윈도우 안에 있는 문자 k의 **개수** |
| `checksecret` | 네 문자 중 **조건을 만족한(개수 ≥ 최소) 문자 수**. 4이면 이 윈도우는 비밀번호로 쓸 수 있다 |

### `checksecret`을 정확히 "같아지는 순간"에만 바꾸는 이유
조건은 "**이상**"인데, 코드는 `==`일 때만 `checksecret`을 바꾼다.

- **추가할 때** (`myadd`): 개수를 1 늘린 **뒤** 최소 개수와 **같아졌다면**, 방금 부족 → 만족으로 바뀐 것이다 → +1. 이미 넘쳐 있던 문자는 더 늘어도 계속 만족이라 바꾸지 않는다.
- **뺄 때** (`myremove`): 개수를 1 줄이기 **전에** 최소 개수와 **같다면**, 줄이는 순간 만족 → 부족으로 떨어진다 → −1. 넘쳐 있던 문자는 하나 빠져도 여전히 만족이다.
- 즉 `checksecret`은 **경계(최소 개수)를 넘나드는 순간에만** 바뀐다. 그래서 확인과 갱신 순서가 add는 "늘리고 → 확인", remove는 "확인 → 줄이고"로 서로 반대다.

### 최소 개수가 0인 문자
- 필요한 개수가 0이면 그 문자는 하나도 없어도 만족이다 → 시작할 때 `checksecret += 1`.
- 이후 그 문자가 들어와도 `mylist`는 1 이상이라 0과 같아질 일이 없고, 빠질 때도 줄이기 전 개수가 1 이상이라 0과 같지 않다. 그래서 한 번 센 만족이 그대로 유지된다.

### 윈도우를 한 칸 미는 방법

```
i = p, j = 0 일 때 (p = 4 예)
 [C C T G] G A T T G      → [C C T G] 에서
  C [C T G G] A T T G     → 오른쪽 G(dna[i]) 추가, 왼쪽 C(dna[j]) 제거
```

- `i` = 새로 들어오는 문자 위치, `j = i - p` = 나가는 문자 위치.
- 추가를 먼저 하고 제거를 나중에 해도 괜찮다. 확인(`checksecret == 4`)은 **둘 다 끝난 뒤**에 하므로, 그 사이에 윈도우가 잠깐 p+1칸이 되는 건 결과에 영향이 없다.

### 처음 윈도우를 따로 처리하는 이유
- 첫 윈도우 [0, p−1]은 "나가는 문자"가 없다. 그래서 `myadd`만 p번 해서 채우고 한 번 확인한다.
- 그 뒤로는 i = p부터 끝까지 "추가 1번 + 제거 1번 + 확인"을 반복한다. 확인하는 윈도우는 처음 1개 + (s − p)개 = **s − p + 1개**로, 길이 p인 모든 부분 문자열과 같다.

### 예제 따라가기 (S = 4, P = 2, `GATA`, 최소 A 1 · C 0 · G 0 · T 1)
- 시작: C, G가 0이라 `checksecret = 2`

| 윈도우 | 추가 / 제거 | A C G T 개수 | checksecret | 결과 |
|---|---|---|---|---|
| GA | G, A 추가 | 1 0 1 0 | 2 + A(1 = 1) = **3** | ✗ |
| AT | T 추가, G 제거 | 1 0 0 1 | 3 + T(1 = 1) = **4** (G는 0 ≠ 0 아님 → 그대로) | ✓ |
| TA | A 추가, A 제거 | 1 0 0 1 | A가 2가 됐다가 다시 1 → 4 그대로 | ✓ |

→ 답 **2**

### 참고: 반복되는 if를 줄이는 방법
`myadd`, `myremove` 안의 네 갈래는 인덱스만 다르고 내용이 같다. 문자를 인덱스로 바꾸는 딕셔너리를 두면 한 갈래로 줄일 수 있다.

```python
IDX = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def myadd(c):
    global checksecret
    k = IDX[c]
    mylist[k] += 1
    if mylist[k] == checklist[k]:
        checksecret += 1
```

결과는 같고, 문자가 늘어나도 딕셔너리만 고치면 된다 ([상하좌우](../../01-implementation/problems/up-down-left-right.md)에서 방향 문자를 딕셔너리로 바꾼 것과 같은 방식).

## 검증
- 예제 `9 8 / CCTGGATTG / 2 0 1 1` → `0`, `4 2 / GATA / 1 0 0 1` → `2`
- 길이 1 ~ 15 무작위 3,000개 입력에서 모든 부분 문자열의 개수를 직접 센 결과와 일치
- S = 1,000,000 (P = 500,000 / P = 10) → 로컬 약 0.3초 / 0.5초

## 배운 점
- **길이 고정 + 연속 구간을 전부 확인** → 슬라이딩 윈도우. 한 칸 밀 때 들어오는 것 1개, 나가는 것 1개만 갱신한다.
- 여러 조건을 매번 다시 확인하지 말고, **만족한 조건의 개수**를 하나 두고 경계를 넘나들 때만 갱신한다.
- 추가는 "늘리고 → 같아졌나", 제거는 "같은가 → 줄이기". 순서가 반대인 이유는 둘 다 **경계를 넘는 순간**을 잡기 위해서다.

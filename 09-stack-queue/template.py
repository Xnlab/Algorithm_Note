import sys
from collections import deque
input = sys.stdin.readline


# ---------- 스택: list ----------
# push: stack.append(x)   pop: stack.pop()   top: stack[-1]   비었나: not stack


def is_valid_brackets(s):
    """괄호 짝 검사 ( ) [ ] { }"""
    pair = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in pair:
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()
    return not stack


def next_greater(arr):
    """오큰수: 각 원소의 오른쪽에서 처음 나오는 더 큰 수 (없으면 -1). 단조 스택 O(N)"""
    ans = [-1] * len(arr)
    stack = []                      # 아직 오큰수를 못 찾은 인덱스들 (값이 내림차순으로 쌓임)
    for i, x in enumerate(arr):
        while stack and arr[stack[-1]] < x:
            ans[stack.pop()] = x
        stack.append(i)
    return ans


# ---------- 큐: deque ----------
# 넣기: q.append(x)   빼기: q.popleft()   맨 앞: q[0]   ※ list.pop(0)은 O(N)이라 쓰지 않는다


def last_card(n):
    """카드 1~n: 맨 위 버리기 → 다음 맨 위를 맨 아래로, 한 장 남을 때까지"""
    q = deque(range(1, n + 1))
    while len(q) > 1:
        q.popleft()
        q.append(q.popleft())
    return q[0]


if __name__ == "__main__":
    assert is_valid_brackets("([]{})") and not is_valid_brackets("(]") and not is_valid_brackets("((")
    assert next_greater([3, 5, 2, 7]) == [5, 7, 7, -1]
    assert next_greater([9, 5, 4, 8]) == [-1, 8, 8, -1]
    assert last_card(6) == 4 and last_card(1) == 1
    print("09-stack-queue OK")

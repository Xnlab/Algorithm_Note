import sys
import heapq
input = sys.stdin.readline


def max_meetings(meetings):
    """(start, end) 리스트 → 겹치지 않게 고를 수 있는 최대 회의 수"""
    meetings.sort(key=lambda x: (x[1], x[0]))   # 끝나는 시간, 같으면 시작 시간
    count, last_end = 0, -1
    for s, e in meetings:
        if s >= last_end:
            count += 1
            last_end = e
    return count


def sort_multi(people):
    """(이름, 나이, 점수) → 점수 내림차순, 나이 오름차순, 이름 사전순"""
    return sorted(people, key=lambda x: (-x[2], x[1], x[0]))


def merge_cost(cards):
    """가장 작은 두 묶음을 반복해서 합칠 때의 최소 총 비용"""
    heapq.heapify(cards)
    total = 0
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        total += a + b
        heapq.heappush(cards, a + b)
    return total


if __name__ == "__main__":
    mt = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10),
          (8, 11), (8, 12), (2, 13), (12, 14)]
    assert max_meetings(mt) == 4
    assert max_meetings([(1, 1), (1, 1), (1, 2)]) == 3

    ppl = [("b", 20, 90), ("a", 25, 90), ("c", 20, 95), ("a", 20, 90)]
    assert sort_multi(ppl) == [("c", 20, 95), ("a", 20, 90), ("b", 20, 90), ("a", 25, 90)]

    assert merge_cost([10, 20, 40]) == 100
    print("03-greedy OK")

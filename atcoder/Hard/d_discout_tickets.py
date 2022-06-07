import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))

def get_min_fee(a, m) -> int:
    a = [(-1)*x for x in a]
    heapq.heapify(a)
    for x in range(m):
        x = heapq.heappop(a)
        heapq.heappush(a, (-x//2)*(-1))
    return -sum(a)



print(get_min_fee(A, M))
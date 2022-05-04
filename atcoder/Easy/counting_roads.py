N, M = map(int, input().split())


def get_load_counts(m, n):
    N = [0]*n
    for i in range(m):
        a, b = map(int, input().split())
        N[a-1] += 1
        N[b-1] += 1

    print(*N, sep='\n')



get_load_counts(M, N)



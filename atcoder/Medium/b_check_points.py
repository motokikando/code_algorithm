from typing import List
n, m = map(int, input().split())
x = [list(map(int, input().split())) for i in [0]*(n+m)]


for a,b in x[:n]:
    l = [abs(a-c)+ abs(b-d) for c, d in x[n:]]
    print(l.index(min(l))+1)



# def get_list(n, m):
#     n_list = [input().split() for i in range(n)]
#     m_list = [input().split() for i in range(m)]
#     return n_list, m_list

# def get_min_distance_spot(n, m) -> List[int]:
#     d = []
#     ans = []
#     N , M = get_list(n, m)
#     for i in range(n):
#         for j in range(m):
#             distance = abs(int(N[i][0]) - int(M[j][0])) + abs(int(N[i][1]) - int(M[j][1]))
#             d.append(distance)
#         ans.append(d.index(min(d))+1)
#         d = []
#     return ans


# for v in get_min_distance_spot(A,B):
#     print(v)




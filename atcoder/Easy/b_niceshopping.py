# from typing import List
# A, B, M = list(map(int, input().split()))
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# X = [list(map(int, input().split()) for i in range(M))]

# def get_resonable(a:List[int], b:List[int], X) -> int:
#     #最小値を追加する
#     ans = [min(a)+ min(b)]

#     #二次元配列のループをする
#     for i, x in enumerate(X):
#         a_idx, b_idx, c = x
#         ans.append(a[a_idx-1]+b[b_idx-1]-c)
#     return min(ans)


# print(get_resonable(a, b, X))
# A, B, M = list(map(int, input().split()))
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# X = [list(map(int, input().split())) for i in range(M)]

# ans = [min(a) + min(b)]
# for x in X:
#     a_idx, b_index, c = x
#     ans.append(a[a_idx - 1] + b[b_index - 1] - c)

# print(min(ans))


x = [10, 11, 13, 13, 14, 14, 17]
mp_obj = map(lambda n: n*3 , x)
fl_obj = filter(lambda n: n%3 == 0, mp_obj)
print(list(fl_obj))

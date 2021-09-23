#　エラーが10以上の

# A, Bに数値を代入できるようにする
A, B = map(int,input().split())
print(A+B if A+B<10 else "error")


def happy_friday(A:int, B:int):
    if A <= 8 and B <= 8:
        print('Yay!')
    else:
        print(':(')



A, B = map(int, input().split())
happy_friday(A, B)
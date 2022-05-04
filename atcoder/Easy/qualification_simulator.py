def judge(ranker:str, a:int, b:int):
    a_sum = 0
    b_sum = 0
    for i in range(len(ranker)):
        if ranker[i] == "a" and (a_sum + b_sum) < a+b:
            a_sum += 1
            print("Yes")
        elif ranker[i] == "b" and (a_sum + b_sum) < a+b and b_sum < b:
            b_sum +=1
            print("Yes")
        else:
            print("No")

n, a, b = map(int, input().split())
s = input()
judge(s, a, b)




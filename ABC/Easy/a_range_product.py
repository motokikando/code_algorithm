A, B = map(int, input().split())

def judge_positive_or_negarive(a:int,b:int):
    if  a > 0 and b > 0:
        return "Positive"
    elif a < 0 and b < 0 and (a+b) % 2 == 1:
        return "Positive"
    elif a <= 0 and b >= 0:
        return "Zero"
    elif a < 0 and b < 0 and (a+b) % 2 == 0:
        return "Negative"

print(judge_positive_or_negarive(A,B))
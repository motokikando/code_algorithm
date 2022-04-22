A = int(input())
B = int(input())

def comparison(a:int, b:int) -> str:
    if a > b:
        return "GREATER"
    elif a < b:
        return "LESS"
    elif a == b:
        return "EQUAL"


print(comparison(A, B))

N = int(input())

def get_modsum(n:int)-> int:
    ans = n*(n-1)//2
    return ans 

print(get_modsum(N))

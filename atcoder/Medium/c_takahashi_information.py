[(a, b, c), (d,e,f),(g,h,i)] = [map(int, input().split()) for i in range(3)]

def get_decision()-> str:
    ans = "No"
    if a - b == d - e == g -h:
        if b -c == e -f == h-i:
            ans = "Yes "
    return ans

print(get_decision())
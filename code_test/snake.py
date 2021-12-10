# 1   5   9
#0 2 4 6 8 0
#   3   7   1

def snake_string(n:int) -> None:
    list_a = []
    list_b = []
    list_c = []

    for i in range(n):
        if  i % 2 == 0:
            list_a.append(' ')
            list_b.append(str(i%10))
            list_c.append(' ')
        elif i % 4 == 1:
            list_a.append(str(i%10))
            list_b.append(' ')
            list_c.append(' ')
        else:
            list_a.append(' ')
            list_b.append(' ')
            list_c.append(str(i%10))
    print(' '.join(list_a))
    print(' '.join(list_b))
    print(' '.join(list_c))


snake_string(60)

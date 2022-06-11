x, a, d, n = map(int, input().split())


if d > 0:
    if a < x < a+(d*(n-1)):
        syo , amari = divmod(x, a+d)
        print(min(abs(x-(a+(d*(syo-1)))) , abs(x-(a+ (d*(syo))))))
    elif a >= x:
        print(abs(a-x))
    else:
        print(abs(x-(a+(d*(n-1)))))


elif d < 0:
    if a+(d*(n-1)) < x < a:
        syo , amari = divmod(x, d)
        print(min(abs(x-((d*(syo-1)))) , abs(x-((d*(syo))))))
    elif a <= x:
        print(abs(x-a))
    else:
        print(abs(x-(a+(d*(n-1)))))

if d ==0:
    print(abs(x-a))
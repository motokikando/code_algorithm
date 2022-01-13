n = 720

lower_divisors , upper_divisors = [], []
i = 1
while i*i <= n:
    if n % i == 0:
        lower_divisors.append(i)
        if i != n // i:
            upper_divisors.append(n//i)
    i += 1
l = lower_divisors + upper_divisors[::-1]
for j in range(len(l)):
    print(l[j])



money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(n**2):
    bag = []
    total = 0
    print("pattern {}:".format(i), end="")

    for j in range(n):
        if (i >> j & 1):
            bag.append(item[j][0])
            total += item[j][1]
    if total <= money:
        print(bag, total)


a = int(input())
if a == 0:
    print(0)
else:
    y, x = 0, 1
    n = 1
    while x <= a:
        if x == a:
            print(n)
            break
        y, x = x, y + x
        n += 1
    else:
        print(-1)

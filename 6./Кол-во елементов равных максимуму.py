x = 0
y = 0
z = -1
while z != 0:
    z = int(input())
    if z > x:
        x, y = z, 1
    elif z == x:
        y += 1
print(y)

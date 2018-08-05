x = int(input())
y = 0
while x != 0:
    z = int(input())
    if z != 0 and x < z:
        y += 1
    x = z
print(y)

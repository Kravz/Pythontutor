n = int(input())
x_power = 2
power = 1
while x_power <= n:
    x_power *= 2
    power += 1
print(power - 1, x_power // 2)

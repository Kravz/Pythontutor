from math import sqrt

x = 0
y = 0
x_i = int(input())
n = 0
while x_i != 0:
    n += 1
    x += x_i
    y += x_i ** 2
    x_i = int(input())
print(sqrt((y - x ** 2 / n) / (n - 1)))

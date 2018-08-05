x = input()
y = ''
for i in range(len(x)):
    if i % 3 != 0:
        y = y + x[i]
print(y)

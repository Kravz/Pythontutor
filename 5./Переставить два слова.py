x = input()
first = x[:x.find(' ')]
second = x[x.find(' ') + 1:]
print(second + ' ' + first)

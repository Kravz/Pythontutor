x = input()
x = x[:x.find('h')] + x[x.rfind('h') + 1:]
print(x)

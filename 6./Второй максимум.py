max1 = int(input())
max2 = int(input())
if max1 < max2:
    max1, max2 = max2, max1
elements = int(input())
while elements != 0:
    if elements > max1:
        max2, max1 = max1, elements
    elif elements > max2:
        max2 = elements
    elements = int(input())
print(max2)

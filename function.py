originalList = ['a', 'b', 'c', 'd']
newList = []
for x in originalList:
    x += 'a'
    newList.append(x)

print(newList)
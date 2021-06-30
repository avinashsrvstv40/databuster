import re
list1 = []
for _ in range(int(input())):
    list1 += re.findall("(?:\w+\.)*\w+\@(?:\w+\.)+\w+", input())
print(*(sorted(set(list1))),sep=';')
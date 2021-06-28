import re
list1 = []
list2 = []
list3 = []
N = int(input())
[list1.append(input()) for _ in range(N)]
q = int(input())
[list2.append(input()) for _ in range(q)]


for j in list2:
    list3 = []
    for i in list1:
        list3.append(len(re.findall(rf"(?<=\w){j}(?=\w)", i)))
    print(sum(list3))
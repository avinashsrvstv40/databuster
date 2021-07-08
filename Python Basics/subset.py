#Method 1 - Without Sets

list = []

for i in range(int(input())):
    lA = int(input())
    p = input().split()
    lB = int(input())
    q = input().split()
    for j in p:
        if j not in q:
            list.append(False)
            break
    else:
        list.append(True)

print(*list, sep = '\n')


#Method 2 - Using Sets

for i in range(int(input())):
    la, p, lb, q = int(input()), set(map(int, input().split())), int(input()), \
    set(map(int, input().split()))
    if p.issubset(q):
        print(True)
    else:
        print(False)
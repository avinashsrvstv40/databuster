from itertools import combinations

l1 = int(input())

l = list(combinations(input().split(), int(input())))

f = [i for i in l if 'a' in i]

print(format(len(f) / len(l), "3f"))
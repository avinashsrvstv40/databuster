N, X = map(int, input().split())
l = []
for i in range(X):
    l.append(map(float, input().split()))


for i in list(zip(*l)):
    print(sum(i) / len(i))
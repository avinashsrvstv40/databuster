n = int(input())
s = set(map(int,input().split()))

for _ in range(int(input())):
    n, *args = input().split()
    if args:
        getattr(s, n)(*(map(int, *args)))
    else:
        getattr(s, n)()

print(sum(s))
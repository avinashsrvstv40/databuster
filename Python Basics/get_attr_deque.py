from collections import deque
d = deque()
for _ in range(int(input())):
    cmd, *args = input().split()
    print(getattr(d, cmd)(*args))
    print(d)
[print(x, end=' ') for x in d]
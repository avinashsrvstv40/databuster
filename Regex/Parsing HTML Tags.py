import re

pat = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'

N = int(input())
for _ in range(N):
    html = input()
    res = re.findall(pat, html)
    for link, title in res:
        print("{0},{1}".format(link, title.strip()))
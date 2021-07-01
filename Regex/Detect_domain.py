import re
N = int(input().strip())
tags = set()
for i in range(N):
    str = input().strip()
    t = re.findall(r"(?:https{0,1}:\/\/(?:ww[w0-9]\.){0,1})([a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9]+)", str)
    for tag in t:
        if tag not in tags:
            tags.add(tag)
taglist = sorted(list(tags))
print(';'.join(taglist))
def pattern(row,column):
    global l
    for i in range(n // 2):
        l.append((".|." * (i * 2 + 1)).center(m, '-'))
    l.append("WELCOME".center(m, '-'))
    for j in range(n // 2, 0, -1):
        l.append((".|." * (j * 2 - 1)).center(m, '-')) 
    return l   



if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    l = []
    result = pattern(n,m)
    print("\n".join(result))
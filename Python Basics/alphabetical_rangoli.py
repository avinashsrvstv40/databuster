import string

def rangoli(num):
    L = []
    for i in range(n):
        s = "-".join(alpha[i:num])
        L.append((s[::-1]+s[1:]).center(4*num-3, "-"))
    return '\n'.join(L[:0:-1]+L)

if __name__ == "__main__":
        
    alpha = string.ascii_lowercase
    n = int(input())
    print(rangoli(n))
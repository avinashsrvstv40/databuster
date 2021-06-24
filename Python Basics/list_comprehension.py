if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    if m == len(A) and m == len(B) and n == len(arr):
        print(sum([1 if i in A else -1 if i in B else 0 for i in arr]))
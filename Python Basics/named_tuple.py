from collections import Counter, defaultdict, namedtuple

if __name__ == "__main__":
    n = int(input())
    sum_marks = 0
    total_students = 0
    avg = namedtuple('avg', input())
    for i in range(n):
        xyz = avg(*input().split())
        sum_marks = sum_marks + int(xyz.MARKS)
        total_students = 1 + total_students
    print(format(sum_marks / total_students, ".2f"))